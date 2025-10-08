import random
from typing import List, Dict, Any
from .agent import ReasoningAgent

class Trainer:
    """
    Reinforcement loop for reasoning agents.
    Evaluates their responses and adjusts curiosity dynamically.
    """

    def __init__(self, agent: ReasoningAgent):
        self.agent = agent
        self.history: List[Dict[str, Any]] = []

    async def feedback_loop(self, prompts: List[str]):
        """Run training loop for a list of prompts."""
        import asyncio
        for p in prompts:
            response = await self.agent.think(p)
            reward = self.evaluate(response)
            self.history.append({"prompt": p, "reward": reward})
            self._adjust_curiosity(reward)
            print(f"[TRAIN] {p[:30]}... → reward={reward:.2f}")

    def evaluate(self, text: str) -> float:
        """Heuristic reward calculation."""
        keywords = ["reason", "reflect", "analy", "pattern", "system"]
        score = sum(k in text.lower() for k in keywords) / len(keywords)
        return round(score + random.uniform(-0.1, 0.1), 2)

    def _adjust_curiosity(self, reward: float):
        """Update agent curiosity based on reward feedback."""
        delta = (reward - 0.5) * 0.2
        self.agent.curiosity = max(0, min(1, self.agent.curiosity + delta))

    def export_history(self) -> List[Dict[str, Any]]:
        """Return training logs."""
        return self.history
