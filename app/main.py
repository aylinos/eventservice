from fastapi import FastAPI

from app.routers import eventrouter, typerouter
from mangum import Mangum  # Amazon Lambda handler

app = FastAPI()

app.include_router(eventrouter.router)
app.include_router(typerouter.router)


# Index route
@app.get("/")
def read_root():
    return {"Eventor": "Welcome to EVENTS service"}


# Get all events
@app.get("/events")
def read_root():
    return {"List of all events"}


handler = Mangum(app=app)  # <----------- wrap the API with Mangum
