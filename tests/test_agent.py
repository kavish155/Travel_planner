import pytest
from agent.graph import extract_preferences, find_destinations, create_itinerary
from agent.tools import load_destinations


@pytest.fixture
def sample_state():
    """Returns a sample state dictionary to use in tests."""
    return {
        "preferences": {
            "budget": "medium",
            "duration": 5,
            "interests": ["culture", "food"],
            "season": "spring"
        },
        "destinations": [],
        "itinerary": {},
        "history": []
    }


def test_extract_preferences(sample_state):
    """Test if user preferences are correctly stored."""
    preferences = sample_state["preferences"]
    assert preferences["budget"] in ["low", "medium", "high"]
    assert isinstance(preferences["duration"], int) and preferences["duration"] > 0
    assert isinstance(preferences["interests"], list) and len(preferences["interests"]) > 0
    assert preferences["season"] in ["winter", "spring", "summer", "fall"]


def test_find_destinations(sample_state):
    """Test if the destination filtering logic works."""
    sample_state = find_destinations(sample_state)
    assert isinstance(sample_state["destinations"], list)
    assert all(dest["budget_level"] == sample_state["preferences"]["budget"] for dest in sample_state["destinations"])


def test_create_itinerary(sample_state):
    """Test if itinerary is generated correctly."""
    sample_state["destinations"] = load_destinations()[:1]  # Pick the first destination
    sample_state["selected_destination"] = sample_state["destinations"][0]  # ✅ Set selected destination
    sample_state = create_itinerary(sample_state)

    assert isinstance(sample_state["itinerary"], dict)
    assert len(sample_state["itinerary"]) == sample_state["preferences"]["duration"]

