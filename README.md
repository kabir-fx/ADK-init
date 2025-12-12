# Agent Development Kit (ADK) Application

This repository contains a Google ADK agent located in the `my_agent` directory.

## Prerequisites

- Python 3.10+
- Google Cloud API Key (for Gemini)

## Setup

1. **Install dependencies: (Inside a virtual env)**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment:**
   Ensure you have a `.env` file in `my_agent/.env` with your API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Running the Application

### 1. Web UI (Recommended)

Launch the visual interface to chat with your agent and see traces:

```bash
# Run from the project root
adk web
```

Access the UI at: http://localhost:8000

### 2. Interactive CLI

Chat with your agent in the terminal:

```bash
adk run my_agent
```

### 3. Production API Server

Start a REST API server for production integration:

```bash
adk api_server --agent_path my_agent/agent.py --host 0.0.0.0 --port 8080
```
