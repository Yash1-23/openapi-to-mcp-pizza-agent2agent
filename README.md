## Mission: Make Pizza AI-Ready

## overview:
This project demonstrate how a traditional pizza API can be made usable by AI agents through
Model Context Protocol(MCP).

Instead of building a new backend logic to a specific LLM, the system converts an OpenAPI specification in to a MCP server
and then proves real-world usability through mutliple co-operating agents.

## Problem Statement:
AI agent is becoming the new interface for users.
Traditional APIs are not directly interact with agents untless they are exposed through a prtocol that supports dicoverability, tool execution, and structured context.

The goal of this project is too:

1.Automatically  translate the OpenAPI specifications into MCP servers.

2.Make pizza APIs accessible to AI agents.

3.Demonstrate agent cooperation through a real world ordering and scheduling workflow like it works as Agent-to-Agent workflow.


## High-Level Architecture



<img width="949" height="464" alt="Architecture_MCP_PIzza_Agent2Agent" src="https://github.com/user-attachments/assets/93b2ce42-a370-4203-b2a5-b88b0c9ef08b" />


## Project Structure

openapi-to-mcp-pizza-agent-to-agent/

│
├── agents/
│   ├── ordering_agent.py
│   └── scheduling_agent.py
│
├── mcp_servers/
│   ├── pizza_mcp_server.py
│   └── calendar_mcp_server.py
│
├── mcp_generator/
│   └── openapi_to_mcp.py
│
├── openapi/
│   └── pizza.yaml
│
├── requirements.txt

├── README.md


## How the System works

1. ## OpenAPI -> MCP
   - Pizza API are defined using an OpenAPI specification.
     
   - A generator reads the OpenAPI file and creates MCP tool definitions.
     
   - The resulting MCP server exposes pizza functionally in a form usable by agents.

2. ## Ordering Agent
   - Accepts the natural language input from the user.
     
   - Uses an LLM to determine which MCP tool to call.
     
   - Calls the Pizza MCP server to place the order.
   
   - Receives structured order dict(order ID,ETA).

3. ## Scheduling Agent(A2A)
   - Receives order details from the Ordering Agent.
  
   - Communicates via Structured data
  
   - Calls a Calender MCP server to Schedule delivery
  
   - Returns confirmation to the user.
  


## Example Run

User I'd like to order the Farmhouse pizza, medium size.

LLM Decision: {

  "tool": "place_order",
  
  "arguments": {
  
   "pizza": "Farmhouse",
   
   "size": "medium"
    
  }
}

 Order Confirmation:
 
{'order_id': 'ORD-3C9617', 'pizza': 'Farmhouse', 'size': 'medium', 'status': 

'confirmed', 'eta_minutes': 30}

 Scheduling Agent received order details:
 
{'order_id': 'ORD-3C9617', 'pizza': 'Farmhouse', 'size': 'medium', 'status':

'confirmed', 'eta_minutes': 30}

 Delivery Scheduled Calendar MCP
 
{'event_id': 'EVT-FE5CFC', 'title': 'pizza delivery for order ORD-3C9617', 

'start_time': '2025-12-26T23:16:54.539691', 'status': 'event created'}


## Setup Instructions

## 1. Create virtual environment

python -m venv venv

source venv/bin/activate   # Windows: venv\Scripts\activate

## 2. Install dependencies

pip install -r requirements.txt

## 3. Start MCP Servers

python mcp_servers/pizza_mcp_server.py

python mcp_servers/calendar_mcp_server.py



## 4. Run the ordering Agent/Scheduling Agent

python agents/ordering_agent.py

python agents/scheduling_agent.py

## 5. Combine both ordering and Scheduling Agent (A2A)

python -m agents.ordering_agent


## Model Compatability

The system is model-agnostic.

Becuase execution is handled by  MCP servers, the ordering agent can use:

- Groq
- Chatgpt
- Gemini

No backend changes are required.

## Conclusion
This project shows how existing APIs can be made AI ready by:

- Translating OpenAPI specifications into MCP servers.

- Using agents as orchestration layers.

- Enabling real-world workflows through agent cooperation.

The focus is on protocol fidelity, clarity and extensibility, rather than model
specific implementations

## Author
 Name : Yashwanth Singh
 
GitHub: https://github.com/Yash1-23

LinkedIn: https://linkedin.com/in/yashwanthsingh










