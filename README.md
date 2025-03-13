# Travel Planner AI Agent

## Overview
The **Travel Planner AI Agent** is an intelligent assistant built using **LangGraph** that helps users plan their trips. It guides users through selecting destinations, generating itineraries, and answering follow-up questions using an **LLM-powered chatbot (Mistral API)** and a **Weather API**.

## Features
- 🌍 **Extract Travel Preferences** (budget, duration, interests, season)
- ✈️ **Recommend Destinations** based on user preferences
- 🗺 **Generate Personalized Itineraries** with location-based activities
- ☁ **Provide Real-Time Weather Updates** for chosen destinations
- 💬 **Answer Follow-up Questions** using an LLM model (Mistral API)
- 🛠 **Handle Errors & Edge Cases Gracefully**

## Technologies Used
- **Python** (3.11)
- **LangGraph** (for multi-step AI workflow)
- **Mistral API** (for follow-up question answering)
- **OpenWeather API** (for weather updates)
- **Pytest** (for testing)

---

## Project Structure
```bash
travel_planner/
├── main.py              # Entry point for the application
├── agent/
│   ├── graph.py         # LangGraph implementation
│   ├── state.py         # State management
│   ├── tools.py         # External tool connections (Weather API, Destination Loader)
├── data/
│   ├── destinations.json # Mock destination database
├── tests/
│   ├── test_agent.py    # Unit tests for different components
└── README.md            # Project documentation
└── requirements.txt     # for downloading packages
```
## Installation & Setup
### Prerequisites
Ensure you have Python 3.11+ installed 

1️⃣** Clone the Repository**
  - git clone <your-repository-url>
  
  - cd travel_planner
    
2️⃣** Set Up Virtual Environment**
  - python -m venv .venv
    
  - source .venv/bin/activate  [ On Windows: .venv\Scripts\activate]

3️⃣** Install Dependencies**
  - pip install -r requirements.txt

4️⃣ **Run the application using:**
  - python main.py


## Example Workflow
1)** Enter Travel Preferences (budget, duration, interests, season)**

2) **Get Recommended Destinations**

3) **Select a Destination**

4) **View a Personalized Itinerary**

5) **Ask Follow-up Questions about weather, activities, best seasons, etc.**

## Testing

### Run test cases using pytest:
- pytest tests/test_agent.py

## Expected tests:

✅ **Preference Extraction**

✅ **Destination Recommendation**

✅ **Itinerary Generation**

✅ **Follow-up Question Handling**


## Error Handling & Edge Cases

✔️ **No matching destinations → Suggest modifying preferences**

✔️ **Invalid destination selection → Prompt user until a valid choice is made**

✔️** API failures (Weather/Mistral) → Provide fallback messages**

✔️ **Nonsense follow-up questions → Guide user to ask relevant queries**

## Submission Requirements

✔️ **Source Code (GitHub/GitLab link)**

✔️ **Documentation (This README file)**

✔️ **Instructions to run the project**

✔️ **Test Cases for major functionalities**

## Resources
- **LangGraph Documentation**
- **Mistral API**
- **OpenWeather API**

