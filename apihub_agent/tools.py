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