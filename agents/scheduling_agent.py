import asyncio
from typing import Dict,Any
from fastmcp import Client

async def scheduling_agent(order_details: Dict[str,Any])-> Dict[str,Any]:
  """
  Scheduling Agent:
  Recives order details from ordering Agent adn scheduling a delivery event using calendar MCP server.
  """
  
  print("\n Scheduling Agent received order details:")
  print(order_details)
  
  #Extract required fields
  order_id = order_details["order_id"]
  eta_minutes = order_details["eta_minutes"]
  
  if eta_minutes is None:
    raise ValueError("Missing required field: eta_minutes")
  
  #connect to calender MCP server
  async with Client("http://127.0.0.1:9000/mcp") as client:
    result = await client.call_tool(
      "create_calendar_event",
      {
        "title":f"pizza delivery for order {order_id}",
        "start_in_minutes": eta_minutes
      }
    )
    
    return result.data
  
  
if __name__=="__main__":
  test_order ={
    "order_id": "ORD-TEST123",
    "eta_minutes": 30
  }
  
  response = asyncio.run(scheduling_agent(test_order))
  
  print("\n Calendar Event Created")
  
  print(response)