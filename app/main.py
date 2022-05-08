from fastapi import FastAPI
from mangum import Mangum  # Amazon Lambda handler
from routers import eventrouter, typerouter

# from app.routers import eventrouter, typerouter

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


handler = Mangum(app=app, lifespan="off")  # <----------- wrap the API with Mangum
