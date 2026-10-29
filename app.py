from fastapi import FastAPI

app = FastAPI(title="Hello World Backend")

@app.get("/api/hello")
def hello():
    return {
        "message": "Hello World from Python Backend!",
        "status": "success",
        "application": "backend-app"
    }

@app.get("/api/health")
def health():
    return {"status": "healthy"}
