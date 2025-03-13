import sys  # ✅ Import sys to allow forced exit
from agent.graph import build_travel_agent
from agent.tools import get_weather

# Build the AI workflow
workflow = build_travel_agent()

def run_ai():
    """Run the travel planner AI."""
    state = {}  # Start with an empty dictionary
    print("Welcome to the Travel Planner AI! 🚀")

    # Run the preference and destination selection steps separately
    for output in workflow.stream(state):
        state = output  # Store the latest state

    # Extract the last step's actual state (removing the step key)
    last_step_key = list(state.keys())[-1]
    state = state[last_step_key]

    # Extract user preferences and recommended destinations
    preferences = state.get("preferences", {})
    recommended_destinations = [d["name"] for d in state.get("destinations", [])]

    print("\nUser Preferences Extracted:", preferences)
    print("\nRecommended Destinations:", recommended_destinations)

    # Let user pick a destination
    if not recommended_destinations:
        print("\n❌ No destinations available. Please restart with different preferences.")
        sys.exit()  # ✅ Stop execution

    while True:
        selected_destination = input("\nWhich destination do you want to visit from the list? ").strip().title()
        destination_data = next((d for d in state["destinations"] if d["name"].lower() == selected_destination.lower()), None)

        if destination_data:
            break
        print("\n❌ Invalid choice! Please select a valid destination from the list.")

    # Generate itinerary based on selection
    generate_itinerary(state, destination_data, preferences.get("duration", 3))

    # ✅ Exit properly if user doesn't want follow-ups
    if not ask_followup_questions(destination_data):
        print("\n🎉 Thank you for using the Travel Planner AI! Have a great trip! 🚀")
        sys.exit()  # ✅ Ensure program exits completely after follow-ups

def generate_itinerary(state, destination, duration):
    """Generate and display itinerary for the selected destination."""
    print(f"\nYour planned trip to {destination['name']}:\n")
    print(f"✅ Best seasons to visit: {', '.join(destination['best_seasons'])}")
    print(f"✅ Budget level: {destination['budget_level']}")
    print(f"✅ Your {duration}-day itinerary:")

    activities = destination.get("activities", [])

    # Fallback if no activities are found
    if not activities:
        activities = [
            f"Explore the city center of {destination['name']}.",
            f"Visit famous landmarks in {destination['name']}.",
            f"Enjoy local food and cultural experiences."
        ]

    for day in range(1, duration + 1):
        print(f"  - Day {day}: {activities[day % len(activities)]}")

def ask_followup_questions(destination):
    """Allows user to ask follow-up questions. Returns False if user exits."""
    print("\nYou can ask follow-up questions about your trip!")
    print("(Type 'exit' to stop asking questions.)\n")

    while True:
        question = input("Ask a question: ").strip().lower()

        if question in ["exit", "no", "no more questions"]:
            print("Okay! Enjoy your trip! 😊")
            return False  # ✅ Return False to indicate the program should stop

        if "weather" in question or "temperature" in question:
            weather_info = get_weather(destination["name"])
            print(f"🔹 {weather_info}")

        elif "best season" in question or "when to visit" in question:
            print(f"🔹 The best seasons to visit {destination['name']} are {', '.join(destination['best_seasons'])}.")

        elif "budget" in question:
            print(f"🔹 {destination['name']} has a {destination['budget_level']} budget level.")

        elif "activities" in question or "things to do" in question:
            print(f"🔹 Here are some things to do in {destination['name']}:")
            for activity in destination["activities"][:5]:  # Show first 5 activities
                print(f"  - {activity}")

        elif "food" in question or "eat" in question:
            print(f"🔹 {destination['name']} is known for its amazing food! Try exploring the local markets and restaurants.")

        elif "history" in question or "culture" in question:
            print(f"🔹 {destination['name']} has a rich history! Make sure to visit historical landmarks and museums.")

        else:
            print("❓ Sorry, I don't have an answer for that. Try asking about activities, best seasons, or budget.")

if __name__ == "__main__":
    run_ai()






