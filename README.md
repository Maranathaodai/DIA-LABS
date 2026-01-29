
# Disaster Response & Relief Coordination System

## Project Overview
This project implements a decentralized multi-agent system for disaster response and relief coordination using Python and the SPADE agent framework. Agents simulate the detection of disaster events, assess environmental conditions, and log disaster details to support rapid, distributed decision-making in uncertain environments.

## What We Did
- Set up a Python development environment with SPADE and XMPP integration
- Created a basic SPADE agent for Lab 1 to verify environment and agent setup
- Developed a detailed SensorAgent for Lab 2 that:
	- Monitors multiple zones (Zone A, Zone B, Zone C, Zone D)
	- Simulates environmental attributes (temperature, humidity, visibility)
	- Detects and logs disaster events (type, severity, affected population, resources needed, timestamp)
	- Structures output by perception cycles for clarity
- Used environment variables for agent credentials and a virtual environment for package management
- Added .gitignore to exclude sensitive and environment-specific files

## Project Structure

```
DIA-LABS/
├── .env                # XMPP credentials (not tracked in git)
├── .gitignore          # Ignore .venv and .env
├── .venv/              # Python virtual environment
├── README.md           # Project description and instructions
├── lab1_basic_agent.py # Lab 1: Basic SPADE agent
├── lab2_sensor_agent.py# Lab 2: SensorAgent with environment modeling
└── disaster_events.log # (Optional) Event logs if file logging is used
```

# How to Run
1. Clone the repository and open in VS Code or GitHub Codespaces
2. Create and activate a Python virtual environment (`python -m venv .venv`)
3. Install dependencies (`pip install spade python-dotenv`)
4. Add your XMPP credentials to `.env`
5. Run the agents:
	 - `python lab1_basic_agent.py` for Lab 1
	 - `python lab2_sensor_agent.py` for Lab 2

## Technologies Used
- Python 3.12+
- SPADE (Smart Python Agent Development Environment)
- XMPP (tested with xmpp.jp)
- GitHub Codespaces / VS Code

## Authors
Your Name(s) Here

## Notes
- The `.env` and `.venv` folders are excluded from version control for security and reproducibility.
- The SensorAgent demonstrates agent perception, environment modeling, and disaster event logging as required by Lab 2.