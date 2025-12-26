from datetime import datetime, timedelta
import uuid
from fastmcp import FastMCP

#create a MCP server
mcp =  FastMCP("Calender MCP Server")


@mcp.tool(name="create_calendar_event")
def create_calender_event(title:str,start_in_minutes:int) -> dict:
  """create a calendar event (used for pizza delivering scheduling)"""
  
  start_time = datetime.now() + timedelta(minutes=start_in_minutes)
  
  
  return {
    "event_id": f"EVT-{uuid.uuid4().hex[:6].upper()}",
    "title": title,
    "start_time": start_time.isoformat(),
    "status":"event created"
  } 
  
          

@mcp.tool()
def list_events() ->dict:    
  """
  List scheduled calendar events (mocked)
  """
  return{
    "message": "Calender service active. Events are created dynamically"
  }
  

if __name__ == "__main__":
  print("Calendar MCP server running on HTTP")
  
  mcp.run(
    transport="http",
    host="127.0.0.1",
    port=9000
  )
  