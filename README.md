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
## Detailed Explanation of Each File & Folder

### 📂 agent/
**This folder contains the core logic of the Travel Planner AI.**

 1) #### graph.py

    - Defines the LangGraph workflow for the AI system.

    - Connects different steps such as extracting preferences, recommending destinations, generating itineraries, and answering follow-up questions.

 2) #### state.py

    - Manages the state of the AI agent, storing user preferences, destinations, and conversation history.

 3) #### tools.py

    Contains helper functions, such as:
  
    - load_destinations() → Loads data from destinations.json.
  
    - get_weather(city) → Fetches real-time weather using the OpenWeather API.
  
### 📂 data/
   
  #### destinations.json
   Stores a list of destinations with details such as:
   
   -  Budget level
     
   - Best seasons

   - Popular activities
   
   - Used for filtering destinations based on user preferences.
   
### 📂 tests/
 
  #### test_agent.py

   Contains unit tests to verify that:
 
   - Preferences are extracted correctly.

   - Destinations are recommended accurately.

   - Itineraries are properly generated.

   - Follow-up question handling works as expected.

 Uses pytest to run automated tests.

## main.py

- The main entry point of the application.

- Handles user input, calls the AI workflow, and displays results.

## requirements.txt

- Lists all required Python dependencies.

- Users can install them with:

   ```pip install -r requirements.txt```

## README.md

- **Project documentation with setup instructions, folder structure,  usage guide, and explanation of files.**

# Installation & Setup
### Prerequisites
Ensure you have Python 3.11+ installed and open Command prompt in windows and 
start writing code step by step given below

1️⃣ **Clone the Repository**
  - ```git clone https://github.com/kavish155/Travel_planner.git```
    
  - ```cd Travel_planner```
    
2️⃣ **Set Up Virtual Environment**
  -  ```python -m venv .venv```
    
  -  ```.venv\Scripts\activate```

3️⃣ **Install Dependencies**

  - ```pip install -r requirements.txt```

4️⃣ **Run the application using:**
  - ```python main.py```

**This 4 steps in command prompt will start the Travel_planner AI**


# Example Workflow
1) **Enter Travel Preferences (budget, duration, interests, season)**

2) **Get Recommended Destinations**

3) **Select a Destination**

4) **View a Personalized Itinerary**

5) **Ask Follow-up Questions about weather, activities, best seasons, etc.**

# Testing

### Run test cases using pytest:
- ```pytest tests/test_agent.py```

## Expected tests:

✅ **Preference Extraction**

✅ **Destination Recommendation**

✅ **Itinerary Generation**

✅ **Follow-up Question Handling**


# Error Handling & Edge Cases

✔️ **No matching destinations → Suggest modifying preferences**

✔️ **Invalid destination selection → Prompt user until a valid choice is made**

✔️ **API failures (Weather/Mistral) → Provide fallback messages**

✔️ **Nonsense follow-up questions → Guide user to ask relevant queries**

# Submission Requirements

✔️ **Source Code (GitHub/GitLab link)**

✔️ **Documentation (This README file)**

✔️ **Instructions to run the project**

✔️ **Test Cases for major functionalities**

# Resources
- **LangGraph Documentation**
- **Mistral API**
- **OpenWeather API**

