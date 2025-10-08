import random
from typing import Dict

class RewardModel:
    """
    RLHF-like reward evaluator.
    Uses heuristic features: clarity, depth, novelty.
    """

    def __init__(self):
        self.criteria: Dict[str, float] = {
            "clarity": 0.3,
            "depth": 0.4,
            "novelty": 0.3
        }

    def score(self, response: str) -> float:
        """Compute weighted reward score."""
        clarity = 1.0 if len(response) < 600 else 0.7
        depth = 1.0 if "reflect" in response.lower() else 0.6
        novelty = random.uniform(0.5, 1.0)

        total = (
            clarity * self.criteria["clarity"]
            + depth * self.criteria["depth"]
            + novelty * self.criteria["novelty"]
        )
        return round(total, 2)

    def critique(self, response: str) -> str:
        """Return textual feedback for agent tuning."""
        score = self.score(response)
        if score > 0.8:
            feedback = "Excellent reasoning depth and novelty."
        elif score > 0.6:
            feedback = "Good clarity; could use deeper reflection."
        else:
            feedback = "Superficial answer — expand reasoning layers."
        return f"Reward={score:.2f} | {feedback}"
