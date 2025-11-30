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
    lvl.add_node(Node("start", (3, 2)))

    lvl.add_node(Node("top_1", (2, 1)))
    lvl.add_node(Node("top_2", (3, 1), "trap"))
    lvl.add_node(Node("top_3", (4, 1), "prize"))

    lvl.add_non_directional_edge("start", "top_1")
    lvl.add_non_directional_edge("start", "top_3")

    lvl.add_non_directional_edge("top_2", "top_3")
    lvl.add_non_directional_edge("top_2", "top_1")

    lvl.add_node(Node("mid_1", (1, 2), "prize"))
    lvl.add_node(Node("mid_2", (2, 2)))
    lvl.add_node(Node("mid_3", (4, 2)))
    lvl.add_node(Node("mid_4", (5, 2), "trap"))

    lvl.add_non_directional_edge("mid_1", "mid_2")
    lvl.add_non_directional_edge("mid_2", "start")
    lvl.add_non_directional_edge("start", "mid_3")
    lvl.add_non_directional_edge("mid_3", "mid_4")

    lvl.add_non_directional_edge("mid_4", "top_3")
    lvl.add_non_directional_edge("mid_1", "top_1")

    lvl.add_node(Node("low", (3, 3)))

    lvl.add_non_directional_edge("low", "start")

    lvl.add_node(Node("bottom", (3, 4), "trap"))
    
    lvl.add_non_directional_edge("bottom", "mid_1")
    lvl.add_non_directional_edge("bottom", "mid_2")
    lvl.add_non_directional_edge("bottom", "low")
    lvl.add_non_directional_edge("bottom", "mid_3")
    lvl.add_non_directional_edge("bottom", "mid_4")

    return lvl

def level_4_graph():
    #Nodes on this graph have been labelled using WASD as (+y, -x, -y, +x)
    lvl = Graph()

    lvl.add_node(Node("start", (1, 3)))

    lvl.add_node(Node("DW", (2, 4)))
    lvl.add_node(Node("DS", (2, 2)))

    lvl.add_edge("start", "DW")
    lvl.add_edge("start", "DS")

    lvl.add_node(Node("WW", (1, 5), "prize"))
    
    lvl.add_non_directional_edge("DW", "WW")
    lvl.add_edge("WW", "start")
    
    lvl.add_node(Node("DD", (3, 3), "prize"))
    lvl.add_node(Node("DDWW", (3, 5), "trap"))

    lvl.add_non_directional_edge("DW", "DD")
    lvl.add_non_directional_edge("DD", "DDWW")
    lvl.add_edge("DDWW", "DW")
    lvl.add_edge("DS", "DD")

    return lvl

def level_5_graph():
    #Nodes on this graph have been labelled with the most direct WASD path to them
    lvl = Graph()
    lvl.add_node(Node("start", (5, 3)))

    lvl.add_node(Node("S", (5, 2), "prize"))
    lvl.add_node(Node("SA", (4, 2)))
    lvl.add_node(Node("SD", (6, 2)))

    lvl.add_non_directional_edge("S", "SA")
    lvl.add_non_directional_edge("S", "SD")
    lvl.add_non_directional_edge("S", "start")

    lvl.add_node(Node("SAS", (4, 1), "trap"))
    lvl.add_node(Node("SDS", (6, 1), "prize"))
    
    lvl.add_non_directional_edge("SD", "SDS")
    lvl.add_non_directional_edge("SA", "SAS")

    lvl.add_node(Node("W", (5, 4)))
    lvl.add_node(Node("WA", (4, 4)))
    lvl.add_node(Node("WD", (6, 4)))

    lvl.add_non_directional_edge("W", "start")
    lvl.add_non_directional_edge("W", "WA")
    lvl.add_non_directional_edge("W", "WD")


    lvl.add_node(Node("WW", (5, 5)))
    lvl.add_node(Node("WWA", (4, 5)))
    lvl.add_node(Node("WAWA", (3, 5), "trap"))
    lvl.add_node(Node("WWD", (6, 5)))
    lvl.add_node(Node("WDWD", (7, 5)))

    lvl.add_non_directional_edge("WA", "WAWA")
    lvl.add_non_directional_edge("WW", "WWA")
    lvl.add_non_directional_edge("WW", "W")
    lvl.add_non_directional_edge("WW", "WWD")
    lvl.add_non_directional_edge("WD", "WDWD")
    

    lvl.add_node(Node("WAWAW", (3, 6)))
    lvl.add_node(Node("WWAW", (4, 6), "prize"))
    lvl.add_node(Node("WWW", (5, 6)))
    lvl.add_node(Node("WWDW", (6, 6), "trap"))
    lvl.add_node(Node("WDWDW", (7, 6)))

    lvl.add_non_directional_edge("WAWAW", "WAWA")
    lvl.add_edge("WWA","WWAW")
    lvl.add_edge("WAWAW", "WWW")
    lvl.add_edge("WWW", "WDWDW")
    lvl.add_edge("WWDW", "WWD")
    lvl.add_non_directional_edge("WDWD", "WDWDW")

    lvl.add_node(Node("WWAWW", (4, 7)))
    lvl.add_node(Node("WWDWW", (6, 7)))

    lvl.add_non_directional_edge("WWAWW", "WWAW")
    lvl.add_non_directional_edge("WWDWW", "WWDW")

    lvl.add_node(Node("WAWAWWW", (3, 8)))
    lvl.add_node(Node("WWWWWWW", (5, 8)))
    lvl.add_node(Node("WDWDWWW", (7, 8)))

    lvl.add_non_directional_edge("WAWAWWW", "WAWAW")
    lvl.add_non_directional_edge("WAWAWWW", "WWAWW")
    lvl.add_non_directional_edge("WWWWWWW", "WWAWW")
    lvl.add_non_directional_edge("WWWWWWW", "WWDWW")
    lvl.add_non_directional_edge("WDWDWWW", "WWDWW")
    lvl.add_non_directional_edge("WDWDWWW", "WDWDW")


    return lvl

def make_level(level_num):
    if level_num == 1:
        lvl = level_1_graph()
    elif level_num == 2:
        lvl = level_2_graph()
    elif level_num == 3:
        lvl = level_3_graph()
    elif level_num == 4:
        lvl = level_4_graph()
    elif level_num == 5:
        lvl = level_5_graph()
    else:
        lvl = level_1_graph()

    return lvl


