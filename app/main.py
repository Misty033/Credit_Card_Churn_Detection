from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Credit Card Churn Prediction API",
    version="1.0.0",
    description="API for predicting credit card churn from CSV input"
)

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Credit Card Churn Prediction API"}
