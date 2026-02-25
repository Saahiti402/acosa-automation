#  ACOSA - AI-Powered Company Operating System Automator

### *Slack → AI → Notion (In Progress) \| Internal Automation System*

ACOSA is a workflow automation engine designed for async-first, remote
teams.\
It listens to Slack messages in real time, analyzes them using an AI
engine, extracts actionable metadata, and prepares them for automated
routing into Notion, Linear, and weekly digest systems.

This project is inspired by remote-first operational systems designed
for clarity, transparency, and async collaboration.

------------------------------------------------------------------------

##  Features Completed So Far

###  Slack → Flask Webhook Listener

-   Real-time Slack Events API integration\
-   Ngrok tunneling for secure external webhook communication\
-   Processes human messages and extracts user, text, and channel
    metadata

###  AI Message Analysis Engine

Offline (no-API) rule-based engine that provides structured analysis: -
Summary generation\
- Type classification: task / update / decision / question / unknown\
- Deadline extraction (e.g., "tomorrow", "Friday")\
- Keyword extraction\
- Owner inference placeholder

LLM-ready: Easily switch to GPT/OpenAI when API credits are available.

###  Modular Automation Architecture

The system is structured to scale:

    Slack → Flask Listener
          → AI Processor
          → Notion Sync (upcoming)
          → Linear Sync (upcoming)
          → Weekly Digest Generator (upcoming)

------------------------------------------------------------------------

##  System Architecture Diagram

    Slack Message
          ↓
    Flask Webhook Listener (slack_listener.py)
          ↓
    AI Engine (ai_engine.py)
          ↓
    Structured Message JSON:
    {
      summary,
      type,
      owner,
      deadline,
      keywords
    }
          ↓
    (Notion Integration - In Progress)
    (Linear Task Creation - In Progress)
    (Weekly AI Digest - In Progress)

------------------------------------------------------------------------

## Tech Stack

-   Python 3.10+\
-   Flask (webhook listener)\
-   Slack Events API\
-   Ngrok (public tunneling)\
-   Offline regex-based AI engine\
-   Optional GPT/OpenAI integration

------------------------------------------------------------------------

##  Project Structure

    acosa-automation/
    │
    ├── slack_listener.py         # Receives Slack events
    ├── ai_engine.py              # Offline AI analysis engine
    ├── notion_client.py          # (In progress) Notion integration module
    ├── weekly_digest.py          # (Upcoming) Weekly digest automation
    └── README.md                 # Project documentation

------------------------------------------------------------------------

##  Roadmap

###  Notion Decision Log Sync

Automatically push structured updates into a Notion database.

###  Linear Task Auto-Creation

Convert Slack updates into structured Linear tasks.

###  Weekly AI Digest

Generate weekly summary of: - Decisions\
- Pending tasks\
- Ownership\
- Team progress

###  Access Provisioning Automation

Future plan: automate workspace permission flows.

------------------------------------------------------------------------

## Setup & Run

### 1. Install dependencies

``` bash
pip install flask
```

(Optional)

``` bash
pip install openai
```

### 2. Start the listener

``` bash
python slack_listener.py
```

### 3. Start ngrok

``` bash
ngrok http 5000
```

### 4. Configure Slack Events API

Add Request URL:

    https://<your-ngrok-subdomain>/slack/events

Enable event:

    message.channels

------------------------------------------------------------------------
