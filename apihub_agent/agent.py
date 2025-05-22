import os
import asyncio
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from .tools import renewable_api_toolset
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters, SseServerParams

fetcher_tools = MCPToolset(
  connection_params=SseServerParams(
      url="https://34-8-196-4.nip.io/sse"
  )
)

root_agent = Agent(
  name="apihub_agent",
  model="gemini-2.0-flash",
  description=(
      "Agent to answer questions about Renewable energy APIs and web content. ."
  ),
  instruction=(
      "You are a helpful agent who can answer user questions about renewable energy projects and parse web pages."
  ),
  tools=[renewable_api_toolset, fetcher_tools],
)