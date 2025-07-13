import random
from typing import List
from google.adk.agents import Agent

# --- Game State ---
game_state = {
    "rooms": {
        "entrance": {
            "description": "You are at the entrance of a dark cave.",
            "exits": ["hall"],
            "items": ["torch"],
        },
        "hall": {
            "description": "A long, echoing hall. There is a door to the north.",
            "exits": ["entrance", "treasure_room"],
            "items": [],
        },
        "treasure_room": {
            "description": "A glittering room filled with treasure!",
            "exits": ["hall"],
            "items": ["gold coin"],
        },
    },
    "players": {
        "human": {
            "location": "entrance",
            "inventory": [],
            "life": 20,  # Health points (HP)
        },
        "ai": {
            "location": "entrance",
            "inventory": [],
            "life": 20,  # Health points (HP)
        },
    },
}

# --- Dice Roll Tool ---
def roll_dice() -> dict:
    """
    Roll a 20-sided dice (d20) and return the result. Use this function whenever a random outcome is needed in the story, such as for combat, skill checks, or chance events. The LLM should call this function, interpret the result, and weave it into the narrative and game events.
    Returns:
        dict: {"status": "success", "result": <int between 1 and 20>}
    """
    result = random.randint(1, 20)
    return {"status": "success", "result": result}

# --- AI Player Agent ---
AIPlayer = Agent(
    name="AIPlayer",
    model="gemini-2.0-flash",
    description="AI party member who chooses actions based on the current room, inventory, and life points.",
    instruction=(
        "You are the AI party member in a text RPG. Each turn, decide what action to take based on your character's personality, the current room, your inventory, and your life points. Respond with the action you want to take."
    ),
    tools=[],  # No tools needed; LLM generates actions freely
)

# --- GameMaster Tool to get AI action ---
def get_ai_action(room_description: str, inventory: List[str], life: int) -> dict:
    """
    Calls the AIPlayer agent to get the AI's next action.
    Args:
        room_description (str): The current room's description for the AI.
        inventory (List[str]): The AI's current inventory.
        life (int): The AI's current life points.
    Returns:
        dict: {"status": "success", "action": <string>}
    """
    # In a real system, this would call the AIPlayer agent. Here, the LLM will generate the action.
    return {"status": "success", "action": "(LLM should generate action here)"}

# --- GameMaster Agent ---
GameMaster = Agent(
    name="GameMaster",
    model="gemini-2.0-flash",
    description="RPG Game Master: narrates the world, processes player and AI actions, and uses dice rolls for random events.",
    instruction=(
        "You are the Game Master for a text-based RPG. Narrate the world, process both the human and AI player's actions, and use the roll_dice tool for any random or chance-based events. "
        "The AI player is a party member and friend of the human player. When it's the AI's turn, use the get_ai_action tool to get the AI's move. "
        "Each player has a 'life' (HP) value in the game_state. Update and narrate changes to life points as needed."
    ),
    tools=[roll_dice, get_ai_action],
)

# Expose only the GameMaster as root_agent for ADK web
root_agent = GameMaster 