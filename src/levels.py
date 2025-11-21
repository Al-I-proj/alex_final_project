from graph import Graph, Node

def level_1_graph():
    #DONE: create a level and create a structure by which coordinates can be manually assigned to the nodes
    lvl_1_graph = Graph()
    lvl_1_graph.add_node(Node("start", coordinates= (3,2)))

    lvl_1_graph.add_node(Node("prize_1", "prize", coordinates= (2, 2)))
    lvl_1_graph.add_node(Node("prize_2", "prize", coordinates= (4, 2)))

    lvl_1_graph.add_node(Node("trap_1", "trap", coordinates= (1, 2)))

    lvl_1_graph.add_edge("start", "prize_1")
    lvl_1_graph.add_edge("prize_1", "start")

    lvl_1_graph.add_edge("start", "prize_2")
    lvl_1_graph.add_edge("prize_2", "start")

    lvl_1_graph.add_edge("prize_1", "trap_1")
    lvl_1_graph.add_edge("trap_1", "prize_1")

    lvl_1_graph.update_trap_and_prize_distances()
    return lvl_1_graph

def level_2_graph():
    lvl_2_graph = Graph()
    lvl_2_graph.add_node(Node("start", coordinates= (5,3)))
    #TODO: design level 2
    

    return lvl_2_graph