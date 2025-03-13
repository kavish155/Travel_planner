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
