import json
import random
from typing import List, Dict, Any

class Memory:
    """
    Dual-layer memory system:
    - short_term: temporary context
    - long_term: stored high-importance reflections
    """

    def __init__(self):
        self.short_term: List[Dict[str, Any]] = []
        self.long_term: List[Dict[str, Any]] = []

    def remember(self, event: str, importance: float):
        """Store an event with given importance."""
        record = {"event": event, "importance": importance}
        self.short_term.append(record)
        if importance >= 0.8:
            self.long_term.append(record)

    def recall(self, query: str) -> List[str]:
        """Retrieve related long-term memories."""
        relevant = [r["event"] for r in self.long_term if query.lower() in r["event"].lower()]
        return relevant[-5:]

    def decay(self, rate: float = 0.05):
        """Simulate memory fading over time."""
        self.long_term = [
            r for r in self.long_term if random.random() > rate * (1 - r["importance"])
        ]

    def export(self) -> str:
        """Export last known memories as JSON."""
        return json.dumps(
            {
                "short_term": self.short_term[-10:],
                "long_term": self.long_term[-50:]
            },
            indent=2
        )
