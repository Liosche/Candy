from fastapi import FastAPI
from analyzer.analyze_text import analyze

app = FastAPI()

@app.post("/message")
async def message_endpoint(payload: dict):
    text = payload.get("text", "")
    result = analyze(text)
    
    # Map 'message' to 'reply' for Android app compatibility
    if "message" in result:
        result["reply"] = result.pop("message")
        
    return result

@app.post("/vision/analyze")
async def vision_analyze(payload: dict):
    return {"reply": "Ich sehe den Bildschirm, kann ihn aber gerade noch nicht voll verarbeiten.", "action": None}

@app.post("/project/create")
async def create_project(payload: dict):
    return {"status": "ok"}

@app.post("/project/add_task")
async def add_task(payload: dict):
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"status": "Candy Backend is running"}
