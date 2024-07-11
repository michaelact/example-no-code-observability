# LLM Stream Application

This application streams responses from a custom LLM (Large Language Model) API using FastAPI and LangChain. It includes a health check endpoint and a web interface to display the streamed responses.

## Setup

### Prerequisites

- [Rancher Desktop](https://rancherdesktop.io/) or [Docker](https://docs.docker.com/engine/install/)

### Installation

1. **Build the Docker image for your application**:

    ```sh
    docker-compose build
    ```

2. **Start the services**:

    ```sh
    docker-compose up
    ```

## Endpoints

### Health Check

- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: Returns the health status of the application.

### Stream

- **Endpoint**: `/stream`
- **Method**: `GET`
- **Description**: Streams the response from the LLM API.
