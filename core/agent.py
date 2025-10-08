import random
import asyncio
from .memory import Memory

class ReasoningAgent:
    """
    Core agent capable of contextual reasoning and self-reflection.
    """

    def __init__(self, name: str):
        self.name = name
        self.memory = Memory()
        self.curiosity = 0.5  # baseline motivation

    async def think(self, prompt: str) -> str:
        """Perform one reasoning cycle."""
        thoughts = [f"[{self.name}] Thinking about: '{prompt}'"]
        await asyncio.sleep(random.uniform(0.1, 0.3))

        # recall
        memory_hits = self.memory.recall(prompt)
        if memory_hits:
            thoughts.append(f"Found {len(memory_hits)} related memories.")
        else:
            thoughts.append("No relevant memories found.")

        # generate reflection
        conclusion = f"Reflection → '{prompt}' connects to higher reasoning patterns."
        importance = min(1.0, random.random() + len(memory_hits) * 0.1)
        self.memory.remember(prompt, importance)

        return "\n".join(thoughts + [conclusion])

    async def reflect(self, prompts: list[str]) -> list[str]:
        """Run reflection across multiple prompts."""
        results = []
        for p in prompts:
            results.append(await self.think(p))
        return results
