





















"""
Agent interaction endpoints.
Provide REST interface for reasoning and reflection.
"""

from fastapi import APIRouter
from core.agent import ReasoningAgent
from core.reward_model import RewardModel

router = APIRouter(prefix="/agent", tags=["Agent"])

agent = ReasoningAgent("NeuroForge-Core")
reward_model = RewardModel()


@router.get("/think")
async def think(prompt: str):
    """Make the agent reason about a prompt."""
    result = await agent.think(prompt)
    score = reward_model.score(result)
    return {
        "agent": agent.name,
        "prompt": prompt,
        "response": result,
        "reward_score": score
    }


@router.get("/reflect")
async def reflect(prompts: list[str]):
    """Run multi-prompt reasoning and return summarized responses."""
    reflections = await agent.reflect(prompts)
    avg_score = sum(reward_model.score(r) for r in reflections) / len(reflections)
    return {"responses": reflections, "average_score": round(avg_score, 2)}
