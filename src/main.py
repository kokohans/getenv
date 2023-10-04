from fastapi import FastAPI
from bin import helper

app = FastAPI()


@app.get("/")
async def root():
    node_info = helper.get_info()
    return node_info