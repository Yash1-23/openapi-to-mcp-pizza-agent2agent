import os
import json
import asyncio
from typing import Dict,Any
from dotenv import load_dotenv
from groq import Groq
from fastmcp import Client
from agents.scheduling_agent import scheduling_agent

#load the env variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
  raise ValueError("GROQ_API_KEY not found in environment")

#Initialize LLM
llm = Groq(api_key=GROQ_API_KEY)

#System prompt for the Ordering Agent
SYSTEM_PROMPT="""
You are a pizza ordering agent.

You MUST respond with ONLY valid JSON.
No explanations. NO markdown. NO extra text.

You can use these MCP tools:
1.list_menu()
2.place_order(pizza: string, size: string)

Rules:
- Valid pizzas: Margherita, Pepperoni, Farmhouse
- Valid sizes: small, medium, large
- If size is missing, default to "medium

Output format:
{
  "tool": "<tool_name>",
  "arguments":{
    "pizza": "<pizza_name>",
    "size": "<size>"
  }
}

"""

async def ordering_agent(user_input: str) ->Dict[str, Any]:
  print("User", user_input)
   
  # Ask LLM what to do
  completion = llm.chat.completions.create(
    model ="llama-3.3-70b-versatile",
    messages=[
         {"role": "system","content":SYSTEM_PROMPT},
         {"role":"user", "content":user_input}
    ],
    temperature=0,
  )
  
  decision_text = completion.choices[0].message.content.strip()
  print("LLM Decision:", decision_text)
  
  
  #Parse LLM output
  decision= json.loads(decision_text)
  
  
  # connect to MCP server over HTTP
  async with Client("http://127.0.0.1:8000/mcp") as client:
      result = await client.call_tool(
        decision["tool"],
        decision.get("arguments",{})
      )
  return result



#Run the agent

if __name__ == "__main__":
  user_request = "I'd like to order the Farmhouse pizza, medium size."
  result = asyncio.run(ordering_agent(user_request))
  
  
  print("\n Order Confirmation:")
  print(result.data)
  
  
  #A2A handoff to scheduling agent
  scheduling_result = asyncio.run(
    scheduling_agent(result.data)
  )
  
  print("\n Delivery Scheduled Calendar MCP")
  print(scheduling_result)
  
  