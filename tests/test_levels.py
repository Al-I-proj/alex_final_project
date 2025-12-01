import pytest

from src.graph import Graph, Node
from src.levels import is_path_to_all_prizes, level_1_graph, level_5_graph


def test_is_path_to_all_prizes():

    assert is_path_to_all_prizes(level_1_graph()) == True
    assert is_path_to_all_prizes(level_5_graph()) == True

    dead_end_graph = Graph()
    
    assert is_path_to_all_prizes(dead_end_graph) == False

    dead_end_graph.add_node(Node("start", (0,0)))
    dead_end_graph.add_node(Node("node 2", (0,0)))
    dead_end_graph.add_edge("start", "node 2")

    assert is_path_to_all_prizes(dead_end_graph) == False

    dead_end_graph.add_node(Node("trap", (0, 0), "trap"))
    dead_end_graph.add_node(Node("prize", (0,0), "prize"))

    dead_end_graph.add_edge("node 2", "trap")
    dead_end_graph.add_edge("trap", "prize")

    assert is_path_to_all_prizes(dead_end_graph) == False

def run_tests():
    test_is_path_to_all_prizes()

run_tests()