# ADK RPG Game Agent

A text-based RPG game framework built with Google ADK, featuring:
- A Game Master agent (LLM-powered) that narrates, manages the world, and processes actions.
- An independent AI party member agent that acts as your in-game friend and companion.
- Dice rolling and health (life/HP) mechanics.
- Designed for use with ADK web.

## Features

- **Text adventure**: Explore rooms, pick up items, and interact with the world.
- **AI Party Member**: The AI agent makes its own decisions and acts as your friend in the party.
- **Dice Rolls**: The Game Master can roll a d20 for random events, combat, and skill checks.
- **Health Tracking**: Both you and the AI have life points (HP) that can change during the adventure.

## Project Structure

```
multi_tool_agent/
  ├── agent.py         # Main agent and tool definitions
  └── __init__.py
```

## Requirements

- Python 3.9+
- Google ADK ([https://github.com/google/adk](https://google.github.io/adk-docs/))
- (Optional) Go (required only for some ADK features, not for this agent)

## Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install ADK and dependencies:**
   ```bash
   pip install google-adk
   ```

4. **(Optional) Install Go**  
   If you see errors about Go not being installed and you need those features, follow instructions at https://go.dev/dl/

## Usage

### Run with ADK Web

1. **Start the ADK web server:**
   ```bash
   adk web multi_tool_agent
   ```

2. **Open your browser** and go to the provided local URL.

3. **Play the game!**
   - The Game Master will narrate the world and prompt you for actions.
   - The AI party member will act independently, making decisions as your in-game friend.
   - Dice rolls and health are managed by the agents.

## Customization

- Edit `multi_tool_agent/agent.py` to add new rooms, items, or mechanics.
- You can expand the game state, add more tools, or customize the AI’s behavior.

## License

MIT (or your preferred license)

## Next Features

- MCP server to connect with Chirp 3
- MCP server to generate images 
