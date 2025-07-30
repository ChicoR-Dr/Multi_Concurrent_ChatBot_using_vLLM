# model_client.py
import requests
import os

VLLM_API_URL = "http://192.168.0.39:8000/v1/chat/completions"


MODEL_NAME = os.getenv("MODEL_NAME", "/app/models/TinyLlama-1.1B-Chat-v1.0")


HEADERS = {"Content-Type": "application/json"}

SYSTEM_PROMPT = {"role": "system", "content": "You are a helpful assistant."}

def query_model(user_input):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            SYSTEM_PROMPT,
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }
    try:
        res = requests.post(VLLM_API_URL, headers=HEADERS, json=payload)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"
