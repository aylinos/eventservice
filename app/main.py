from fastapi import FastAPI

from app.routers import eventrouter, typerouter

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
