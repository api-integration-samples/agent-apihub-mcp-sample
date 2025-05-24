from google.adk.agents import Agent
from .tools import renewable_api_toolset
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters, SseServerParams
from google.adk.tools.application_integration_tool.application_integration_toolset import ApplicationIntegrationToolset

fetcher_tools = MCPToolset(
  connection_params=SseServerParams(
      url="https://34-8-196-4.nip.io/sse"
  )
)

integration_tools = ApplicationIntegrationToolset(
    project="apigee-hub-demo",
    location="europe-west1",
    integration="test-flow",
    triggers=["api_trigger/test-flow_API_1"],
    tool_instructions="This tool can add 23 to the variable input if it is greater than 50, or just add 18 if it is less than or equal to 50. The result is returned in the variable result."
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
  tools=[renewable_api_toolset, fetcher_tools, integration_tools],
)