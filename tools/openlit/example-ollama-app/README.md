# LLM Stream Application

This application uses LangChain and OpenLit to interact with a Large Language Model (LLM) using the Ollama service. It sends random prompts to the LLM, reasks the same prompts, and repeats this process 50 times.

## Setup

### Prerequisites

- [Rancher Desktop](https://rancherdesktop.io/) or [Docker](https://docs.docker.com/engine/install/)
- https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image

### Installation

1. **Build the Docker image for your application**:

    ```sh
    docker-compose build
    ```

2. **Start the services**:

    ```sh
    docker-compose up
    ```

## Simple Flow

1. **Initialization**: The script initializes the OpenLit environment and the LLM with the specified model and base URL.
2. **Random Prompts**: It prepares a list of random prompts.
3. **Looping**: The script runs a loop 50 times:
   - Chooses a random prompt from the list.
   - Sends the prompt to the LLM and prints the response.
   - Reasks the same prompt and prints the response again.
