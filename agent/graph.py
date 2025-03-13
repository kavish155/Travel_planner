from langgraph.graph import StateGraph
from agent.tools import load_destinations, get_weather
import random
import sys  # ✅ Import sys to allow forced exit
import requests
import os
MISTRAL_API_KEY = "iRutAbQsP1M6RgS8CgLxs9u97bw3Ev03"  # ✅ Recommended: Set this in your system environment
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"


def extract_preferences(state_dict: dict) -> dict:
    """Ask the user for travel preferences and update the state."""
    print("\nLet's plan your trip! Please answer the following questions:")

    # Budget validation
    valid_budgets = {"low", "medium", "high"}
    while True:
        budget = input("Enter your budget (low/medium/high): ").strip().lower()
        if budget in valid_budgets:
            break
        print("❌ Invalid input! Please enter 'low', 'medium', or 'high'.")

    # Duration validation
    while True:
        try:
            duration = int(input("How many days do you want to travel? ").strip())
            if duration > 0:
                break
            print("❌ Duration must be a positive number.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

    # Interests validation
    while True:
        interests = input("Enter your interests (comma-separated, e.g., culture, food, adventure): ").strip().lower()
        interests_list = [interest.strip() for interest in interests.split(",") if interest.strip()]
        if interests_list:
            break
        print("❌ Please enter at least one valid interest.")

    # Season validation
    valid_seasons = {"winter", "spring", "summer", "fall"}
    while True:
        season = input("What season are you planning to travel? (winter/spring/summer/fall): ").strip().lower()
        if season in valid_seasons:
            break
        print("❌ Invalid input! Please enter 'winter', 'spring', 'summer', or 'fall'.")

    state_dict["preferences"] = {
        "budget": budget,
        "duration": duration,
        "interests": interests_list,
        "season": season
    }
    return state_dict


def find_destinations(state_dict: dict) -> dict:
    """Find destinations based on user preferences."""
    destinations = load_destinations()
    filtered_destinations = [
        d for d in destinations
        if d["budget_level"] == state_dict["preferences"]["budget"]
        and any(tag in state_dict["preferences"]["interests"] for tag in d["tags"])
    ]

    if not filtered_destinations:
        print("\n❌ No destinations match your preferences. Try different criteria.")
        sys.exit()  # Stop execution safely

    state_dict["destinations"] = filtered_destinations
    return state_dict



def select_destination(state_dict: dict) -> dict:
    """Allow the user to select a destination from the recommended list."""
    recommended_destinations = [d["name"] for d in state_dict["destinations"]]

    if not recommended_destinations:
        print("\n❌ No destinations available. Please restart with different preferences.")
        sys.exit()

    print("\nRecommended Destinations:", recommended_destinations)

    while True:
        selected_destination = input("\nWhich destination do you want to visit from the list? ").strip().title()
        destination_data = next((d for d in state_dict["destinations"] if d["name"].lower() == selected_destination.lower()), None)

        if destination_data:
            state_dict["selected_destination"] = destination_data
            return state_dict  # ✅ Exit loop & continue execution

        print("❌ Invalid choice! Please select from the recommended list.")  # Keep prompting


def create_itinerary(state_dict: dict) -> dict:
    """Generate an itinerary based on the chosen destination."""
    if "selected_destination" not in state_dict:
        print("❌ No destination selected. Cannot create an itinerary.")
        sys.exit()  # ✅ Stop execution

    chosen_destination = state_dict["selected_destination"]
    duration = state_dict["preferences"]["duration"]
    activities = chosen_destination.get("activities", [])

    if not activities:
        activities = [
            f"Explore the city center of {chosen_destination['name']}.",
            f"Visit famous landmarks in {chosen_destination['name']}.",
            f"Enjoy local food and cultural experiences."
        ]

    random.shuffle(activities)
    itinerary = {f"Day {day}": activities[day % len(activities)] for day in range(1, duration + 1)}

    state_dict["itinerary"] = itinerary

    # ✅ Print itinerary before asking follow-up questions
    print(f"\nYour planned trip to {chosen_destination['name']}:\n")
    print(f"✅ Best seasons to visit: {', '.join(chosen_destination['best_seasons'])}")
    print(f"✅ Budget level: {chosen_destination['budget_level']}")
    print(f"✅ Your {duration}-day itinerary:")
    for day, activity in itinerary.items():
        print(f"  - {day}: {activity}")

    return state_dict



def handle_followup(state_dict: dict) -> dict:
    """Handles user follow-up questions using Mistral API."""
    print("\nYou can ask follow-up questions about your trip! (Type 'exit' to stop)")

    while True:
        user_question = input("\nAsk a follow-up question: ").strip()

        if user_question.lower() in ["exit", "no", "no more questions"]:
            print("Okay! Enjoy your trip! 😊")
            sys.exit()  # ✅ Stops execution immediately after follow-ups

        city = state_dict["selected_destination"]["name"]
        full_prompt = (
            f"You are a travel assistant. The user is traveling to {city}. "
            f"Answer their question based on the best travel knowledge:\n\nUser: {user_question}\nAI:"
        )

        response = query_mistral(full_prompt)
        print(f"🔹 {response}")

    return state_dict


def build_travel_agent():
    """Ensure the workflow runs in the correct order and stops properly."""
    workflow = StateGraph(dict)

    workflow.add_node("extract_preferences", extract_preferences)
    workflow.add_node("find_destinations", find_destinations)
    workflow.add_node("select_destination", select_destination)
    workflow.add_node("create_itinerary", create_itinerary)
    workflow.add_node("handle_followup", handle_followup)

    workflow.add_edge("extract_preferences", "find_destinations")
    workflow.add_edge("find_destinations", "select_destination")
    workflow.add_edge("select_destination", "create_itinerary")
    workflow.add_edge("create_itinerary", "handle_followup")

    workflow.set_entry_point("extract_preferences")
    workflow.set_finish_point("handle_followup")  # ✅ Ensures workflow properly stops

    return workflow.compile()


def query_mistral(prompt):
    """Query Mistral API to generate responses."""
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-medium",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200
    }

    response = requests.post(MISTRAL_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return "⚠️ Error: Unable to get a response from Mistral."




