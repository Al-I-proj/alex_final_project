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

def level_3_graph():
    
    lvl = Graph()
    lvl.add_node(Node("start", (5, 2)))

    lvl.add_node(Node("top_1", (4, 1), "trap"))
    lvl.add_node(Node("top_2", (5, 1), "prize"))
    lvl.add_node(Node("top_3", (6, 1)))

    lvl.add_non_directional_edge("start", "top_1")
    lvl.add_non_directional_edge("start", "top_3")

    lvl.add_non_directional_edge("top_2", "top_3")
    lvl.add_non_directional_edge("top_2", "top_1")

    lvl.add_node(Node("mid_1", (3, 2), "prize"))
    lvl.add_node(Node("mid_2", (4, 2)))
    lvl.add_node(Node("mid_3", (6, 2)))
    lvl.add_node(Node("mid_4", (7, 2), "prize"))

    lvl.add_non_directional_edge("mid_1", "mid_2")
    lvl.add_non_directional_edge("mid_2", "start")
    lvl.add_non_directional_edge("start", "mid_3")
    lvl.add_non_directional_edge("mid_3", "mid_4")

    lvl.add_non_directional_edge("mid_4", "top_3")
    lvl.add_non_directional_edge("mid_1", "top_1")

    lvl.add_node(Node("bottom", (5, 4), "trap"))
    
    lvl.add_non_directional_edge("bottom", "mid_1")
    lvl.add_non_directional_edge("bottom", "mid_2")
    lvl.add_non_directional_edge("bottom", "start")
    lvl.add_non_directional_edge("bottom", "mid_3")
    lvl.add_non_directional_edge("bottom", "mid_4")

    return lvl