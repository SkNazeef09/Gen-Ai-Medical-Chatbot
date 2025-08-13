import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.prompt import system_prompt

# --- Environment variable handling ---
HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    print("⚠️  Warning: HF_TOKEN not found in environment variables.")
    print("   → The app will run in local mode, but Hugging Face API features won't work.")

# --- FastAPI app initialization ---
app = FastAPI(title="Gen-AI Medical Chatbot")

@app.get("/")
async def home():
    if not HF_TOKEN:
        return {"message": "HF_TOKEN is missing. Running in local mode."}
    return {"message": "HF_TOKEN detected. Ready to use Hugging Face API."}

# Example chat endpoint
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    question = data.get("question", "")

    if not question:
        return JSONResponse({"error": "No question provided"}, status_code=400)

    if not HF_TOKEN:
        # Offline fallback
        return {"answer": f"[Offline mode] You asked: '{question}'. API access is disabled."}

    # --- Your RAG pipeline logic here ---
    # Example: response = rag_chain.invoke({"input": question})
    # return {"answer": response["answer"]}

    return {"answer": "Example answer (replace with real RAG logic)"}
