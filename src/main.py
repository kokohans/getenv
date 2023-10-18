from fastapi import FastAPI, Response, status
from bin import helper

app = FastAPI()


@app.get("/")
async def root():
    node_info = helper.get_info()
    return node_info

@app.get("/healthz")
async def get_health_status(response: Response):

    node_health = helper.get_health()

    match node_health['system_status']:
        case 'healthy':
            response.status_code = status.HTTP_200_OK
        case 'unhealthy':
            response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        case _:
            response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return node_health