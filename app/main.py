from fastapi import FastAPI

app = FastAPI(
    title="Hello Cloud API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Hello Kubernetes"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}