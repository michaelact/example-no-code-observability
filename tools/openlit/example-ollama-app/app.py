import openlit
import random
from langchain_community.llms import Ollama

# Initialize OpenLit with the specified environment and application name
openlit.init(environment="development", application_name="example-chat-app-michaelact", collect_gpu_stats=True)

# Initialize the LLM with the specified model and base URL
llm = Ollama(
    model="mixtral",
    base_url="http://172.22.2.19:11434"
)  # assuming you have Ollama installed and have llama3 model pulled with `ollama pull llama3 `

# List of random prompts
prompts = [
    "Tell me a joke",
    "What is the weather like today?",
    "Can you share a fun fact?",
    "What's the capital of France?",
    "Who won the last soccer world cup?",
    "What's your favorite color?",
    "Tell me a riddle",
    "How does a car engine work?",
    "What is quantum physics?",
    "Can you explain the theory of relativity?"
]

# Loop 50 times
for i in range(50):
    # Choose a random prompt
    prompt = random.choice(prompts)
    print("Bertanya", prompt)

    # Invoke the LLM with the chosen prompt
    response1 = llm.invoke(prompt)
    print(f"Response {i*2+1}: {response1}")

    # Reask the same prompt
    response2 = llm.invoke(prompt)
    print(f"Response {i*2+2}: {response2}")
