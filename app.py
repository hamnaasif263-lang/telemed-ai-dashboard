from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create FastAPI instance
# The variable is named 'app', which is required by the uvicorn app:app command.
app = FastAPI(title="telemedicine AI Dashboard", version="1.0")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the telemedicine AI Dashboard!"}

# Example endpoint: health check
@app.get("/health")
def health_check():
    return {"status": "OK"}

# Example endpoint: echo query parameter
@app.get("/echo")
def echo(message: str):
    return {"echoed_message": message}