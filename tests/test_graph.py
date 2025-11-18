import pytest

from src.graph import Graph, Node

def make_graph_1():
    
    test_graph_1 = Graph()
    test_graph_1.add_node(Node("root"))
    test_graph_1.add_node(Node("L"))
    test_graph_1.add_node(Node("R"))

    test_graph_1.add_edge("root","L")
    test_graph_1.add_edge("root","R")

    test_graph_1.add_node(Node("LL"))
    test_graph_1.add_node(Node("LR"))

    test_graph_1.add_edge("L","LL")
    test_graph_1.add_edge("L","LR")
    
    test_graph_1.add_node(Node("RL"))
    test_graph_1.add_node(Node("RR"))

    test_graph_1.add_edge("R","RL")
    test_graph_1.add_edge("R","RR")
    return test_graph_1

def test_find_nodes_at_distance():
    test_graph_1 = make_graph_1()

    assert test_graph_1.find_nodes_at_distance("root", 2) == ["LL", "LR", "RL", "RR"]

def test_find_distance_of_node_type():
    test_graph_2 = make_graph_1()
    test_graph_2.add_node(Node("RRL", "trap"))
    test_graph_2.add_edge("RR", "RRL")

    trap_distance = test_graph_2.find_distance_from_nearest_node_of_type("root", "trap")
    assert trap_distance == 3

def run_tests():
    #test_find_nodes_at_distance()
    test_find_distance_of_node_type()

run_tests()