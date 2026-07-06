import requests
import json

payload = {
    "user_id": "karan",
    "budget": 50000000,
    "population": 100000,
    "current_state": {
        "healthcare": 200,
        "education": 60,
        "water": 80000,
        "sanitation": 70000,
        "transport": 200,
        "green_space": 500000,
        "housing": 25000,
        "electricity": 95
    },
    "priorities": {
        "healthcare": 1.5,
        "water": 1.3,
        "housing": 1.2,
        "education": 1.0,
        "sanitation": 1.0,
        "transport": 0.8,
        "green_space": 0.7,
        "electricity": 1.2
    }
}

response = requests.post("http://localhost:8000/plan", json=payload)
print(json.dumps(response.json(), indent=2))