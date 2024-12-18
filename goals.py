import requests
from typing import Optional
from dotenv import load_dotenv
import os
import json

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "70e53c75-b286-41b0-a591-03f7ec33dbf3"
APPLICATION_TOKEN = os.getenv("LANGFLOW_TOKEN")

def get_suggestion(profile, physical_goals, mental_goals):
    TWEAKS = {
    "TextInput-BDaux": {
        "input_value": profile
    },
    "TextInput-fewLJ": {
        "input_value":physical_goals
    },
    "TextInput-4Nl0R": {
        "input_value": mental_goals
    }
    }
    return run_flow("", tweaks=TWEAKS, application_token=APPLICATION_TOKEN)

def run_flow(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:

    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/goals"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return json.loads(response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"])

result=get_suggestion("""age: 28 years,  
weight: 75 kg,  
height: 175 cm,  
gender: male,  
daily activity: high,  
sleeping pattern: 7-8 hours per night,  
work schedule: 9 AM - 5 PM, desk job.  ""","Endurance improvement", "Stress management")

print(result)