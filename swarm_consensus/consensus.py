"""Multi-agent consensus algorithms."""
from typing import Dict, Any, List, Optional
from collections import Counter

class SwarmConsensus:
    def __init__(self, quorum_ratio: float = 0.5):
        self.quorum_ratio = quorum_ratio
        self.votes: Dict[str, Any] = {}
        self.weights: Dict[str, float] = {}

    def register_vote(self, agent_id: str, vote_option: Any, weight: float = 1.0) -> None:
        self.votes[agent_id] = vote_option
        self.weights[agent_id] = weight

    def compute_winner(self) -> Optional[Any]:
        if not self.votes:
            return None
        tallies: Dict[Any, float] = {}
        total_weight = sum(self.weights.values())

        for agent, opt in self.votes.items():
            w = self.weights.get(agent, 1.0)
            tallies[opt] = tallies.get(opt, 0.0) + w

        winner, top_weight = max(tallies.items(), key=lambda x: x[1])
        if (top_weight / total_weight) >= self.quorum_ratio:
            return winner
        return None
