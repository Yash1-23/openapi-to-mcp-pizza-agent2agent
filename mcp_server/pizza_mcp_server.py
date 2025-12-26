#!/usr/bin/env python3
"""
Pizza MCP Server (HTTP Transport)
Stable on Windows
"""

import uuid
from datetime import datetime
from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Pizza Order Server")

# Mock data
MENU = ["Margherita", "Pepperoni", "Farmhouse"]
ORDERS = {}

@mcp.tool()
def list_menu() -> dict:
    """Return available pizzas"""
    return {
        "pizzas": MENU
    }

@mcp.tool()
def place_order(pizza: str, size: str) -> dict:
    """Place a pizza order"""
    if pizza not in MENU:
        return {
            "error": "Invalid pizza",
            "available_pizzas": MENU
        }

    order_id = f"ORD-{uuid.uuid4().hex[:6].upper()}"

    ORDERS[order_id] = {
        "pizza": pizza,
        "size": size,
        "status": "confirmed",
        "eta_minutes": 30,
        "created_at": datetime.now().isoformat()
    }

    return {
        "order_id": order_id,
        "pizza": pizza,
        "size": size,
        "status": "confirmed",
        "eta_minutes": 30
    }

@mcp.tool()
def get_order_status(order_id: str) -> dict:
    """Get order status"""
    if order_id not in ORDERS:
        return {"error": "Order not found"}

    return ORDERS[order_id]


if __name__ == "__main__":
    print("Pizza MCP Server running on HTTP")
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000
    )
