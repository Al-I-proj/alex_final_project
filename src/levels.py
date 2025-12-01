from graph import Graph, Node
import random

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

    lvl.add_node(Node("start", (1, 2)))

    lvl.add_node(Node("DW", (2, 3)))
    lvl.add_node(Node("DS", (2, 1)))

    lvl.add_edge("start", "DW")
    lvl.add_edge("start", "DS")

    lvl.add_node(Node("WW", (1, 4), "prize"))
    
    lvl.add_non_directional_edge("DW", "WW")
    lvl.add_edge("WW", "start")
    
    lvl.add_node(Node("DD", (3, 2), "prize"))
    lvl.add_node(Node("DDWW", (3, 4), "trap"))

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

def random_graph(node_count: int, directional: bool, restart: bool = True):
    lvl = Graph()
    existing_coordinates = {}
    all_x_values = []
    x = random.randint(1, node_count//2)
    y = random.randint(1, node_count//4)
    lvl.add_node(Node("start", (x, y)))
    prizes = max(1, node_count//10)
    traps = max(1, node_count//10)
    prize_count = 0
    trap_count = 0

    for _ in range(node_count - 1):
        x = random.randint(1, node_count//2)
        y = random.randint(1, node_count//4)
        while x in existing_coordinates and y in existing_coordinates[x]:
            x += 1
            x = x % (node_count // 2)
            y += 1
            y = y % (node_count // 2)
        if x in existing_coordinates:
            existing_coordinates[x] += [y]
        else:
            existing_coordinates[x] = [y]
        if x not in all_x_values:
            all_x_values += [x]
        #TODO: make code to randomly assign node type

        lvl.add_node(Node(f"{x},{y}", (x,y)))

    for this_x in all_x_values:
        close_xs = []
        close_x_distance = 1
        if this_x in existing_coordinates:
            if len(existing_coordinates[this_x]) > 1:
                close_xs += [this_x]
        while len(close_xs) < 1:
            if this_x + 1 in existing_coordinates:
                close_xs += [this_x + close_x_distance]
            if this_x - 1 in existing_coordinates:
                close_xs += [this_x - close_x_distance]
            close_x_distance += 1

        for this_y in existing_coordinates[this_x]:
            this_node_id = f"{this_x},{this_y}"
            pot_connections = []
            close_y_distance = 1
            while len(pot_connections) < 1:
                for close_x in close_xs:
                    for close_x_y in existing_coordinates[close_x]:
                        if abs(close_x_y - this_y) <= close_y_distance:
                            pot_connections += [(close_x, close_x_y)]
            connection_count = random.randint(1, len(pot_connections))
            for _ in range(connection_count):
                i = random.randint(0, len(pot_connections) - 1)
                random_node_id = f"{pot_connections[i][0]},{pot_connections[i][1]}"
                repeat = False

                if this_node_id in lvl.edges:
                    if random_node_id in lvl.edges[this_node_id]:
                        repeat = True
                tested_i = []
                while repeat and len(tested_i) <= len(pot_connections):
                    tested_i += [i]
                    i += 1
                    i = i % len(pot_connections)
                    random_node_id = f"{pot_connections[i][0]},{pot_connections[i][1]}"
                    if random_node_id in lvl.edges[this_node_id]:
                        repeat = True
                if not repeat:
                    connection_count -= 1
                    if directional:
                        lvl.add_edge(this_node_id, random_node_id)
                    else:
                        lvl.add_non_directional_edge(this_node_id, random_node_id)
                    pot_connections.pop(i)

    lvl, prize_indices = random_node_data_assignment(lvl, "prize", prizes)
    
    lvl = random_node_data_assignment(lvl, "trap", traps, prize_indices)[0]

    while not is_path_to_all_prizes(lvl):
        lvl = add_random_close_edges(lvl, all_x_values, existing_coordinates, directional, 1)
    
    return lvl


    
def add_random_close_edges(lvl, all_x_values, existing_coordinates, directional, connection_count):
    for this_x in all_x_values:
        close_xs = []
        close_x_distance = 1
        if this_x in existing_coordinates:
            if len(existing_coordinates[this_x]) > 1:
                close_xs += [this_x]
        while len(close_xs) < 1:
            if this_x + 1 in existing_coordinates:
                close_xs += [this_x + close_x_distance]
            if this_x - 1 in existing_coordinates:
                close_xs += [this_x - close_x_distance]
            close_x_distance += 1

        for this_y in existing_coordinates[this_x]:
            this_node_id = f"{this_x},{this_y}"
            pot_connections = []
            close_y_distance = 1
            while len(pot_connections) < 1:
                for close_x in close_xs:
                    for close_x_y in existing_coordinates[close_x]:
                        if abs(close_x_y - this_y) <= close_y_distance:
                            pot_connections += [(close_x, close_x_y)]
            connection_count = random.randint(1, len(pot_connections))
            for _ in range(connection_count):
                i = random.randint(0, len(pot_connections) - 1)
                random_node_id = f"{pot_connections[i][0]},{pot_connections[i][1]}"
                repeat = False

                if this_node_id in lvl.edges:
                    if random_node_id in lvl.edges[this_node_id]:
                        repeat = True
                tested_i = []
                while repeat and len(tested_i) <= len(pot_connections):
                    tested_i += [i]
                    i += 1
                    i = i % len(pot_connections)
                    random_node_id = f"{pot_connections[i][0]},{pot_connections[i][1]}"
                    if random_node_id in lvl.edges[this_node_id]:
                        repeat = True
                if not repeat:
                    connection_count -= 1
                    if directional:
                        lvl.add_edge(this_node_id, random_node_id)
                    else:
                        lvl.add_non_directional_edge(this_node_id, random_node_id)
                    pot_connections.pop(i)
    return lvl

def random_node_data_assignment(lvl, data, new_assignment_count, excluded = []):
    random_indices = []
    for _ in range(new_assignment_count):
        random_node_index = random.randint(0, len(lvl.nodes_list)-1)
        while random_node_index in random_indices or random_node_index in excluded:
            random_node_index += 1
            random_node_index = random_node_index % len(lvl.nodes_list)
        random_indices += [random_node_index]
    for i in random_indices:
        lvl.nodes[lvl.nodes_list[i]].data = data
    return lvl, random_indices


def is_path_to_all_prizes(lvl):
    visits = {}
    return prize_path_recursive(lvl, "start", 0, visits)

def prize_path_recursive(lvl: Graph, current_node_id, prize_count, visits: dict):
    if "start" not in lvl.nodes:
        return False
    
    if lvl.total_prizes < 1:
        return False
    
    if prize_count == lvl.total_prizes:
        return True
    
    if current_node_id in visits:
        visits[current_node_id] += 1
    else:
        visits[current_node_id] = 1
    if current_node_id in lvl.edges:
        if visits[current_node_id] > len(lvl.edges[current_node_id]):
            return False
    else:
        return False
    
    for child_id in lvl.edges[current_node_id]:
        this_child_path = False
        if lvl.nodes[child_id].data == "prize":
            prize_count += 1

        if lvl.nodes[child_id].data != "trap":
            this_child_path = prize_path_recursive(lvl, child_id, prize_count, visits)
        if this_child_path:
            return True
    
    return False




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

def test_prize_path_recursive():
    
    dead_end_graph = Graph()
    
    if is_path_to_all_prizes(dead_end_graph) == False:
        print("Passed")
    else:
        print("Failed: empty graph")

    dead_end_graph.add_node(Node("start", (0,0)))
    dead_end_graph.add_node(Node("node 2", (0,0)))
    dead_end_graph.add_edge("start", "node 2")

    if is_path_to_all_prizes(dead_end_graph) == False:
        print("Passed")
    else:
        print("Failed: no prize")

    dead_end_graph.add_node(Node("trap", (0, 0), "trap"))
    dead_end_graph.add_node(Node("prize", (0,0), "prize"))

    dead_end_graph.add_edge("node 2", "trap")
    dead_end_graph.add_edge("trap", "prize")

    if is_path_to_all_prizes(dead_end_graph) == False:
        print("Passed")
    else:
        print("Failed: prize blocked by trap")
    
    dead_end_graph.nodes["trap"].data = ""

    if is_path_to_all_prizes(dead_end_graph) == True:
        print("Passed")
    else:
        print("Failed: direct prize path (directional)")

    dead_end_graph.add_node(Node("prize_2", (0,0), "prize"))
    dead_end_graph.add_edge("start", "prize_2")
    
    if is_path_to_all_prizes(dead_end_graph) == False:
        print("Passed")
    else:
        print("Failed: no singular path")
    
