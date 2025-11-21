from graph import Graph, Node

def level_1_graph():
    #DONE: create a level and create a structure by which coordinates can be manually assigned to the nodes
    lvl_1_graph = Graph()
    lvl_1_graph.add_node(Node("start", (3,2)))

    lvl_1_graph.add_node(Node("prize_1", (2, 2), "prize"))
    lvl_1_graph.add_node(Node("prize_2", (4, 2), "prize" ))

    lvl_1_graph.add_node(Node("trap_1", (1, 2), "trap"))

    lvl_1_graph.add_non_directional_edge("start", "prize_1")

    lvl_1_graph.add_non_directional_edge("start", "prize_2")

    lvl_1_graph.add_non_directional_edge("prize_1", "trap_1")

    lvl_1_graph.update_trap_and_prize_distances()
    return lvl_1_graph

def level_2_graph():
    lvl = Graph()
    lvl.add_node(Node("start", (5,3)))
    #TODO: design level 2
    lvl.add_node(Node("-1,-1", (4,2)))
    lvl.add_node(Node("1,-1", (6,2)))

    lvl.add_non_directional_edge("start", "-1,-1")
    lvl.add_non_directional_edge("start", "1,-1")

    lvl.add_node(Node("-2,-2", (3, 1), "trap"))
    lvl.add_node(Node("0,-2", (5, 1), "prize"))
    lvl.add_node(Node("2,-2", (7, 1), "prize"))

    lvl.add_non_directional_edge("-1,-1", "-2,-2")
    lvl.add_non_directional_edge("-1,-1", "0,-2")
    
    lvl.add_non_directional_edge("1,-1", "0,-2")
    lvl.add_non_directional_edge("1,-1", "2,-2")
  

    return lvl