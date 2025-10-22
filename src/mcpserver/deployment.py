# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Calculator MCP Server")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Multiply an addition tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


# Subtract an addition tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

# Division an addition tool
@mcp.tool()
def divide(a: int, b: int) -> int:
    """divicdivide two numbers"""
    return a / b

if __name__ == "__main__":
    mcp.run()