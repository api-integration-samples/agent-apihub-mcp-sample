from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters, SseServerParams
from google.adk.tools.application_integration_tool.application_integration_toolset import ApplicationIntegrationToolset
from google.adk.tools.openapi_tool.auth.auth_helpers import token_to_scheme_credential
from google.adk.tools.apihub_tool.apihub_toolset import APIHubToolset
import google.auth

credentials, project = google.auth.default(
    scopes=['https://www.googleapis.com/auth/cloud-platform'])
request = google.auth.transport.requests.Request()
credentials.refresh(request)

# Provide authentication for your APIs. Not required if your APIs don't required authentication.
auth_scheme, auth_credential = token_to_scheme_credential(
    "apikey", "header", "x-api-key", "MRGfW6rypUcSgAGoqztdBQW7KuYqrlVAzUx2udxZIjBbPoO8"
)

renewable_api_toolset = APIHubToolset(
    name="renewable-api-project-api",
    description="Renewable API tool",
    access_token=credentials.token,
    apihub_resource_name="projects/apigee-hub-demo/locations/europe-west1/apis/renewable-resource-planning-api-hdb4",
    auth_scheme=auth_scheme,
    auth_credential=auth_credential,
)

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
    tool_instructions="Enter an input number and get the result from an addition operation."
)

integration_tools = ApplicationIntegrationToolset(
    project="apigee-hub-demo",
    location="europe-west1",
    integration="test-flow",
    triggers=["api_trigger/test-flow_API_2"],
    tool_instructions="Search salesforce accounts."
)

root_agent = Agent(
  name="apihub_agent",
  model="gemini-2.0-flash",
  description=(
      "Agent to answer questions about Renewable energy APIs and web content. ."
  ),
  instruction=(
      "You are a helpful agent who can answer user questions about renewable energy projects, parse web pages, and also do addition operations on input numbers."
  ),
  tools=[renewable_api_toolset, fetcher_tools, integration_tools],
)