from fastapi import FastAPI

app = FastAPI()


# Index route
@app.get("/")
def read_root():
    return {"Eventor": "Welcome to EVENTS service"}
