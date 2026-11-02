"""Unit tests for SwarmConsensus."""
import unittest
from swarm_consensus.consensus import SwarmConsensus

class TestSwarmConsensus(unittest.TestCase):
    def test_weighted_consensus(self):
        c = SwarmConsensus(quorum_ratio=0.5)
        c.register_vote("a1", "commit", weight=2.0)
        c.register_vote("a2", "abort", weight=1.0)
        c.register_vote("a3", "abort", weight=0.5)
        self.assertEqual(c.compute_winner(), "commit")

    def test_no_quorum(self):
        c = SwarmConsensus(quorum_ratio=0.8)
        c.register_vote("a1", "opt1", 1.0)
        c.register_vote("a2", "opt2", 1.0)
        self.assertIsNone(c.compute_winner())

if __name__ == "__main__":
    unittest.main()
