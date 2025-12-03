from fastapi import FastAPI, Body
from pydantic import BaseModel
import uvicorn
from src.api.v1 import routers
from src.db.db import create_db_and_tables 

app = FastAPI()
# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()

create_db_and_tables()
app.include_router(routers.router, prefix="/api/v1")
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
