#  Product Search MCP Server

This provides a lightweight **MCP (Model Context Protocol)** server using **Python** and **OpenSearch**, designed to be used as a custom tool with **Claude**. Users can ask product-related queries (e.g., “give detail about monitor ”) and Claude will respond using real OpenSearch data via your MCP tool.

##  Features

- Natural language product search
- Claude-compatible MCP tool server
- Environment-based OpenSearch credentials
- Lightweight and extensible Python FastMCP setup

##  Project Structure
    product_search_mcp/
    │
    ├── product_server.py # MCP server with product search tool
    ├── .env # Stores OpenSearch credentials
    ├── README.md 
    └── claude_desktop_config.json

## Create and activate virtual environment
    uv venv
    .venv\Scripts\activate   

## Install Dependencies
    uv add mcp[cli] opensearch-py python-dotenv

##  Claude Integration
1. Add this to your Claude's **claude_desktop_config.json**
2. Restart Claude Desktop.
3. Ask something like:
    give detail about jersey?

## Requirements
    |Python 3.10+
    |Claude desktop with MCP support
    |OpenSearch index 