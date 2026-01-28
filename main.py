WEBHOOK_URL = os.getenv("APOLLO_WEBHOOK_URL")

@app.post("/enrich")
def enrich(payload: dict):
    email = payload.get("email")
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")

    body = {
        "email": email,
        "reveal_phone_number": True,
        "webhook_url": WEBHOOK_URL
    }

    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": APOLLO_API_KEY
    }

    response = requests.post(
        "https://api.apollo.io/v1/people/match",
        json=body,
        headers=headers
    )

    return {
        "status": "submitted",
        "apollo_response": response.json()
    }
