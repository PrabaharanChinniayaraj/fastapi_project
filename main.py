from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Employee API is running"
    }