import os
from zoneinfo import ZoneInfo
from google.adk.agents import LlmAgent
from .tools import renewable_api_toolset
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters, SseServerParams

async def get_tools_async():

  local_tools = []
  local_tools = local_tools + renewable_api_toolset.get_tools()

  # fetcher_tools, exit_stack = await MCPToolset.from_server(
  #   connection_params=SseServerParams(
  #        url="https://fetcher-mcp-server-609874082793.europe-west1.run.app/sse"
  #   )
  # )
  
  fetcher_tools, exit_stack = await MCPToolset.from_server(
    connection_params=SseServerParams(
         url="https://34-8-196-4.nip.io/sse"
    )
  )
  
  local_tools = local_tools + fetcher_tools + renewable_api_toolset.get_tools()

  return local_tools, exit_stack

async def get_agent_async():
  local_tools, exit_stack = await get_tools_async()

  root_agent = LlmAgent(
      name="apihub_agent",
      model="gemini-2.0-flash",
      description=(
          "Agent to answer questions about Renewable energy APIs and web content. ."
      ),
      instruction=(
          "You are a helpful agent who can answer user questions about renewable energy projects and parse web pages."
      ),
      tools=local_tools,
  )
  
  return root_agent, exit_stack
  
root_agent = get_agent_async()