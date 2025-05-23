# API Hub ADK Sample

## Install
```sh
# create new virtual environment
python -m venv .venv
# activate venv
source .venv/bin/activate
# install packages
pip install -r requirements.txt
```

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