from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welcome_message():
    return {"message": "Welcome to YOUR Friend in Editing!"}