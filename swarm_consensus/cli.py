"""Command line interface for swarm-consensus."""
from .consensus import SwarmConsensus

def main():
    sc = SwarmConsensus(quorum_ratio=0.5)
    sc.register_vote("agent_coder", "OptionA", weight=1.5)
    sc.register_vote("agent_reviewer", "OptionA", weight=1.0)
    sc.register_vote("agent_tester", "OptionB", weight=1.0)
    print("Consensus Winner:", sc.compute_winner())

if __name__ == "__main__":
    main()
