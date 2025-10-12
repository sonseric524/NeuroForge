"""
NeuroForge Backend — FastAPI entrypoint.
Provides REST & WebSocket access to the Reasoning Agent,
training interface, and memory visualization.
"""

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from core.agent import ReasoningAgent
from core.trainer import Trainer
from core.reward_model import RewardModel
import asyncio
import uvicorn
import logging

# ======================================================
# ⚙️ App Initialization
# ======================================================

app = FastAPI(
    title="NeuroForge API",
    version="0.1.0",
    description="Cognitive backend for reasoning agent system."
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("neuroforge")

# Core instances
agent = ReasoningAgent("NeuroForge-Core")
trainer = Trainer(agent)
reward_model = RewardModel()


# ====================================================

