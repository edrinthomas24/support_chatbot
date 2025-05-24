from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import chat, knowledge, auth
from .services.vector_store import init_vector_store

app = FastAPI(title="Internal Support Chatbot")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(knowledge.router)

@app.on_event("startup")
async def startup_event():
    await init_vector_store()
