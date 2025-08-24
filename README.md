# MCP Server

This repository contains a simple [Model Context Protocol](https://arxiv.org/abs/2305.01697) (MCP) server implemented with FastAPI. The server exposes two endpoints that are compatible with the ChatGPT connectors feature.

## Endpoints

### POST `/search`
Accepts a JSON body with a `query` string and returns search results from your data source. Currently the implementation returns dummy results but you can customise it to return real content.

### POST `/fetch`
Accepts a JSON body with a list of document `ids` and returns the document content.

## Running locally

1. Clone this repository:

    ```bash
    git clone https://github.com/vivekprajapat305/mcp-server.git
    cd mcp-server
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Start the server:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

The server will run on `http://localhost:8000`.

## Connecting to ChatGPT

To connect this MCP server to ChatGPT, follow these steps:

1. Deploy the server to a publicly accessible URL (e.g., using a cloud service like Render, Heroku, or your own server).
2. In ChatGPT's "Actions" or "Connectors" settings, choose to add a new MCP connector and enter the base URL of your running server (e.g., `https://your-domain.com`).
3. ChatGPT will automatically discover the `/search` and `/fetch` endpoints and allow you to ask questions against your data.

## Customising

The current implementation in `main.py` includes placeholder logic. You should replace the `search` and `fetch` functions with your own logic to retrieve data from your actual sources.
