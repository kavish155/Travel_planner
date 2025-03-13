from typing import Dict, List, Any

class AgentState:
    def __init__(self):
        self.preferences: Dict[str, Any] = {}  # Stores user preferences
        self.destinations: List[Dict[str, Any]] = []  # Stores suggested destinations
        self.itinerary: Dict[str, Any] = {}  # Stores generated itinerary
        self.history: List[Dict[str, str]] = []  # Stores conversation history

    def update_preferences(self, preferences: Dict[str, Any]):
        """Update user travel preferences."""
        self.preferences.update(preferences)

    def add_destination(self, destination: Dict[str, Any]):
        """Add a recommended destination."""
        self.destinations.append(destination)

    def set_itinerary(self, itinerary: Dict[str, Any]):
        """Store the generated itinerary."""
        self.itinerary = itinerary

    def add_history(self, user_message: str, ai_response: str):
        """Save conversation history."""
        self.history.append({"user": user_message, "ai": ai_response})

    def reset(self):
        """Reset state for a new planning session."""
        self.__init__()

    def to_dict(self):
        """Convert the state object into a dictionary."""
        return {
            "preferences": self.preferences,
            "destinations": self.destinations,
            "itinerary": self.itinerary,
            "history": self.history
        }

    @staticmethod
    def from_dict(state_dict):
        """Convert a dictionary back into an AgentState object."""
        state = AgentState()
        state.preferences = state_dict.get("preferences", {})
        state.destinations = state_dict.get("destinations", [])
        state.itinerary = state_dict.get("itinerary", {})
        state.history = state_dict.get("history", [])
        return state

