# main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from model_client import query_model
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
    with open("static/index.html") as f:
        return f.read()

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    reply = query_model(user_input)
    return JSONResponse({"response": reply})