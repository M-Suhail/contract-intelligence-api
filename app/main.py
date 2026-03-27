from fastapi import FastAPI

app = FastAPI(
    title="Contract Intelligence API",
    description="Upload contracts and extract key terms using AI.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "name": "Contract Intelligence API",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}