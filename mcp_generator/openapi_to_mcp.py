# 1. Load OpenAPI spec
# 2. Loop through paths
# 3. For each method:
#    - Create MCP tool name
#    - Generate input schema
#    - Attach handler function
# 4. Register tool with MCP server
#spec: OpenAPI file converted into a python dict

"""
OpenAPI → MCP Tool Generator

Purpose:
- Parse an OpenAPI 3.0 specification
- Automatically generate MCP-compatible tool definitions
- Enable AI agents to discover and invoke REST APIs via MCP

Design assumptions:
- Supports GET and POST methods
- Focuses on requestBody + path params
- Backend logic is mocked (not production REST)
"""

import yaml
def load_openapi_spec(file_path: str) -> dict :    
  ## Load OpenAPI YAML file
   with open(file_path,"r") as f:
     return yaml.safe_load(f)

def extract_mcp_tools(openapi:dict) -> list:
    "Convert OpenAPI specification to MCP tool definitions."
    
    mcp_tools= []
    
    paths = openapi.get("paths",{})
    for _, methods in paths.items():
        for _, spec in methods.items():
            tool ={
              "name": spec.get("operationId"),
              "description": spec.get("summary",""),
              "input_schema": spec.get("requestBody",{}).get("content",{}),
              "response_schema": spec.get("responses",{})
              
              
            }
            mcp_tools.append(tool)
    return mcp_tools
  
  
  
  
## Test the above mcp tool
if __name__ == "__main__":
  spec = load_openapi_spec("D:\Pizza_mcp\openapi\pizza.yaml")
  tools = extract_mcp_tools(spec)
  
  for t in tools:
    print(t["name"], "->", t["description"])