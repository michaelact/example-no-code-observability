from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse
from langchain import PromptTemplate, LLMChain
from langchain.llms.base import LLM
import os
import openlit
import httpx
import uvicorn
import time
from typing import Optional, List

openlit.init()

# Initialize FastAPI
app = FastAPI()
llm_api_url = os.getenv("LLM_API_URL", "http://llm:80/generate_stream")

# Custom LLM class to use the external LLM service
class CustomLLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "custom"

    async def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        async with httpx.AsyncClient() as client:
            async with client.stream("POST", llm_api_url, json={"inputs": prompt}) as response:
                if response.status_code != 200:
                    raise HTTPException(status_code=response.status_code, detail=await response.text())
                async for line in response.aiter_lines():
                    yield line

# Initialize the custom LLM
llm = CustomLLM()

# Define the prompt template and LLMChain
template = "Human: What is the capital of France?\nAI:"
prompt = PromptTemplate(template=template, input_variables=["message"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

@app.get("/health")
async def health():
    return JSONResponse(content={"status": "ok"})

@app.get("/stream")
async def stream():
    async def event_generator():
        try:
            async for token in llm._call(prompt="What is the capital of Indonesia?"):
                yield f"data: {token}\n\n"
                time.sleep(0.1)  # Simulate streaming by adding delay
        except Exception as e:
            yield f"data: Error - {str(e)}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

@app.get("/")
async def get_root():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Stream Response</title>
        </head>
        <body>
            <h1>Response Stream</h1>
            <div id="response"></div>
            <script>
                const eventSource = new EventSource("/stream");
                eventSource.onmessage = function(event) {
                    const responseDiv = document.getElementById("response");
                    responseDiv.innerHTML += event.data + " ";
                };
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
