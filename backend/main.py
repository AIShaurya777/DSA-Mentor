from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://dsa-mentor-4mzi99of-dsa-mentor.vercel.app",
        "https://dsa-mentor-pied.vercel.app",
    ],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}
