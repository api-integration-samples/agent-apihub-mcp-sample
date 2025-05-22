# API Hub ADK Sample

## Deploy
```sh
GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
GOOGLE_CLOUD_LOCATION="europe-west1"
AGENT_PATH="./multi_tool_agent"
SERVICE_NAME="apihub-agent"
APP_NAME="apihub-agent"

# deploy fetcher mcp server to cloud run
gcloud run services replace fetcher-cloudrun.yaml --project $GOOGLE_CLOUD_PROJECT --region $GOOGLE_CLOUD_LOCATION

adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name=$SERVICE_NAME \
--app_name=$APP_NAME \
--with_ui \
$AGENT_PATH
```