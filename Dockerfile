# ADK RPG Game Agent - Docker image for Fly.io
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ADK web expects a directory whose *subdirectories* are agent packages (each with __init__.py + agent.py)
# So we put our agent at agents/multi_tool_agent/ and run: adk web agents
COPY multi_tool_agent/ agents/multi_tool_agent/

# ADK web listens on PORT (Fly.io sets PORT=8080)
ENV PORT=8080
EXPOSE 8080

# Run from /app; adk web agents finds agents/multi_tool_agent/ as one agent
CMD ["/bin/sh", "-c", "adk web agents --host 0.0.0.0 --port ${PORT}"]
