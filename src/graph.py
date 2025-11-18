class Node:
    def __init__(self, node_id, data = "", trap_distance = 0, prize_distance = 0):
        self.node_id = node_id
        self.data = data
        self.children_types = []
        self.children_list = []
        self.children = {
            "all":[]
        }
        self.trap_distance = trap_distance
        self.prize_distance = prize_distance
    
    def __str__(self):
        children = self.children["all"]
        return f"({self.node_id}, {children})"
    
    def __repr__(self):
        children = self.children["all"]
        return f"({self.node_id}, {children})"

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.nodes_list = []

    def add_node(self, node):
        self.nodes[node.node_id] = node
        self.nodes_list += [node.node_id]

    def add_edge(self, node_id_1, node_id_2):
        node_1 = self.nodes[node_id_1]
        node_2 = self.nodes[node_id_2]

        self.edges[node_id_1] = node_id_1
        node_1.children_list += [node_id_2]
        

    def find_distance_from_nearest_node_of_type(self, root_node_id, data):
        found = False
        i = 1
        while not found:
            nodes_at_distance_i = self.find_nodes_at_distance(root_node_id, i)
            for this_node_id in nodes_at_distance_i:
                if not found:
                    if self.nodes[this_node_id].data == data:
                        found = True
            if not found:
                i += 1
        return i

    def find_nodes_at_distance(self, root_node_id, distance):
        root_node = self.nodes[root_node_id]
        if distance < 1:
            return []
        if distance == 1:
            return root_node.children_list
        if len(root_node.children) == 0:
            return []

        nodes_at_distance = []

        for child in root_node.children_list:
            nodes_at_distance += self.find_nodes_at_distance(child, distance - 1)
        
        return nodes_at_distance

    def update_trap_and_prize_distances(self):
        for this_node_id in self.nodes_list:
            self.nodes[this_node_id].trap_distance = self.find_distance_from_nearest_node_of_type(this_node_id, "trap")
            self.nodes[this_node_id].prize_distance = self.find_distance_from_nearest_node_of_type(this_node_id, "prize")
             
