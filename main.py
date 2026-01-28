from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

@app.post("/enrich")
def enrich(payload: dict):
    email = payload.get("email")
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")

    url = "https://api.apollo.io/v1/people/match"

    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": APOLLO_API_KEY
    }

    body = {
        "email": email,
        "reveal_phone_number": True
    }

    response = requests.post(url, json=body, headers=headers)
    return response.json()
