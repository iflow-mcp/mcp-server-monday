import asyncio
import sys
import os

from . import fastmcp_server

def main():
    """Main entry point for the package."""
    # Check if we should use stdio mode (for MCP testing)
    if "--stdio" in sys.argv or os.getenv("MCP_STDIO_MODE"):
        asyncio.run(run_stdio_server())
    else:
        asyncio.run(fastmcp_server.run_server())

async def run_stdio_server():
    """Run the server in stdio mode for MCP compatibility."""
    from .fastmcp_server import mcp, monday_client, MondayClient, MONDAY_API_KEY
    
    # Initialize the Monday client
    global monday_client
    monday_client = MondayClient(MONDAY_API_KEY)
    
    # Run with stdio transport
    await mcp.run_async(transport="stdio")

__all__ = ["main", "fastmcp_server", "run_stdio_server"]