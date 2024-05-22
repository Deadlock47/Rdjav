import os
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from src.routes import jav, non_jav, rss

app = FastAPI()
app.include_router(jav.router)
app.include_router(non_jav.router)
app.include_router(rss.router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(request: Request):
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(
        app=app, host="localhost", port=int(os.getenv("PORT", "8080")), use_colors=False
    )
