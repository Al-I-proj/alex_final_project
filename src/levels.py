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

def random_graph(total_nodes: int, directional: bool):
    lvl = Graph()
    existing_coordinates = {}
    all_xs = []

    planned_prizes = max(1, total_nodes // 10)
    planned_traps = max(1, total_nodes // 10)


    x_max = total_nodes // 2
    y_max = total_nodes // 4

    x = random.randint(1, x_max)
    y = random.randint(1, y_max)
    lvl.add_node(Node(f"start", (x, y)))
    all_xs += [x]
    existing_coordinates[x] = [y]

    special_nodes = {
        x:y
    }

    prize_path_lengths = random_path_lengths(planned_prizes, total_nodes)

    for path_length in prize_path_lengths:
        lvl, this_prize_node, path_coordinates, path_xs = generate_random_path(lvl, lvl.nodes["start"], "prize", special_nodes,
                                                    2, x_max, y_max, path_length, directional, all_xs)
        special_nodes = combine_dictionary_of_lists(special_nodes, this_prize_node)
        for this_x in path_xs:
            if this_x not in all_xs:
                all_xs += [this_x]
    
    trap_path_lengths = random_path_lengths(planned_traps, total_nodes, 2)

    for path_length in trap_path_lengths:
        lvl, this_trap_node, path_coordinates, path_xs = generate_random_path(lvl, lvl.nodes["start"], "trap", special_nodes,
                                                    2, x_max, y_max, path_length, directional, all_xs)
        special_nodes = combine_dictionary_of_lists(special_nodes, this_trap_node)
        for this_x in path_xs:
            if this_x not in all_xs:
                all_xs += [this_x]

    while len(lvl.nodes) < total_nodes:
        i = random.randint(1, len(lvl.nodes_list))
        this_node = lvl.nodes[lvl.nodes_list[i]]
        new_x, new_y = generate_random_next_coordinate(existing_coordinates, this_node.coordinates, 2,
                                        x_max, y_max)
        new_node_id = f"{new_x},{new_y}"
        lvl.add_node(Node(new_node_id, (new_x, new_y)))
        lvl.add_non_directional_edge(this_node.node_id, new_node_id)
    return lvl



    
def generate_random_next_coordinate(existing_coordinates, this_coordinate, acceptable_distance, x_max, y_max):
    x = max(1, min(x_max, this_coordinate[0] + random.randint(-acceptable_distance, acceptable_distance)))
    y = max(1, min(y_max, this_coordinate[1] + random.randint(-acceptable_distance, acceptable_distance)))

    repeat_coordinate = True

    tested_y = 0
    tested_x = 0
    while repeat_coordinate:
        repeat_coordinate = False
        if x in existing_coordinates:
            if y in existing_coordinates[x]:
                repeat_coordinate = True
                if tested_y < acceptable_distance * 2:
                    y_modifier = y - this_coordinate[1]
                    y_modifier %= acceptable_distance
                    y = this_coordinate[1] + y_modifier + 1
                    tested_y += 1
            if tested_x < acceptable_distance * 2:
                x_modifier = x - this_coordinate[0]
                x_modifier %= acceptable_distance
                x = this_coordinate[0] + x_modifier
                tested_x += 1
                tested_y = 0
            if tested_x > acceptable_distance:
                acceptable_distance += 1


    return (x, y)
    
def random_path_lengths(num_paths, total_nodes, min_length = 1):
    path_lengths = [total_nodes//num_paths]*num_paths
    for path_length_index in range(len(path_lengths)):
        transfer_index = random.randint(0, len(path_lengths)-1)
        transfer_amount = random.randint(0, path_lengths[path_length_index] -1 - min_length)
        path_lengths[path_length_index] -= transfer_amount
        path_lengths[transfer_index] += transfer_amount
    return path_lengths

def generate_random_path(lvl, start_node, path_end_data, unavailable_end_nodes, acceptable_distance, x_max, y_max, path_length
                         , directional, all_xs):
    existing_nodes = {}
    remaining_path_length = path_length
    last_node = start_node
    all_xs = []
    while remaining_path_length >= 0:
        if remaining_path_length == 0:
            next_x, next_y = generate_random_next_coordinate(combine_dictionary_of_lists(existing_nodes, unavailable_end_nodes, all_xs), last_node.coordinates, 
                                                            acceptable_distance, x_max, y_max)
        else:
            next_x, next_y = generate_random_next_coordinate(existing_nodes, last_node.coordinates, 
                                                            acceptable_distance, x_max, y_max)
        next_node_id = f"{next_x},{next_y}"
        if next_x in existing_nodes:
            existing_nodes[next_x] += [next_y]
        else:
            existing_nodes[next_x] = [next_y]
            all_xs += [next_x]

        if next_node_id not in lvl.nodes:
            lvl.add_node(Node(next_node_id, (next_x, next_y)))
        
        if remaining_path_length == 0:
            if next_node_id in lvl.nodes:
                lvl.nodes[next_node_id].data = path_end_data

        if directional:
            lvl.add_edge(last_node.node_id, next_node_id)
        else:
            lvl.add_non_directional_edge(last_node.node_id, next_node_id)
        remaining_path_length -= 1

    return lvl, {next_x:next_y}, existing_nodes, all_xs

def combine_dictionary_of_lists(d1: dict, d2: dict, key_list: list):
    combined_dict = {}
    for key in key_list:
        if key in d1:
            if key in combined_dict:
                for entry in d1[key]:
                    if entry not in combined_dict[key]:
                        combined_dict[key] += [entry]
            else:
                combined_dict[key] = d1[key]
        if key in d2:
            if key in combined_dict:
                for entry in d2[key]:
                    if entry not in combined_dict[key]:
                        combined_dict[key] += [entry]
            else:
                combined_dict[key] = d2[key]
    return combined_dict


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
        #lvl = random_graph(level_num * 2, False)

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
    
random_graph(12, False)