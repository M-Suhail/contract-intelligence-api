from fastapi import FastAPI
from app.routers import contracts

app = FastAPI(
    title="Contract Intelligence API",
    description="Upload contracts and extract key terms using AI.",
    version="1.0.0"
)

# Register the contracts router
# Same as app.use('/contracts', contractsRouter) in Express
app.include_router(contracts.router)


@app.get("/")
def root():
    return {
        "name": "Contract Intelligence API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}