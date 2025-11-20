import pygame

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


def run_game():
    lvl = level_1_graph()

    pygame.init()
    #TODO: create system to display and interact with a graph

    screen = pygame.display.set_mode((1280, 720))
    square_size = 100
    clock = pygame.time.Clock()
    running = True

    player_position = pygame.Vector2(lvl.nodes["start"].x * square_size, lvl.nodes["start"].y * square_size)
    
    visited_nodes = []
    last_player_position = player_position
    player_node_id = "start"
    player_node = lvl.nodes[player_node_id]

    up_nodes = []
    down_nodes = []
    left_nodes = []
    right_nodes = []
    starting = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame

        # RENDER YOUR GAME HEREscreen.fill("purple")
        for this_node_id in lvl.nodes_list:
            current_setup_node = lvl.nodes[this_node_id]
            if this_node_id in lvl.edges:
                for child in lvl.edges[this_node_id]:
                    pygame.draw.line(screen, "white", 
                                     pygame.Vector2(current_setup_node.x * square_size, current_setup_node.y  * square_size),
                                      pygame.Vector2(lvl.nodes[child].x * square_size, lvl.nodes[child].y * square_size), 
                                      5)
            color = "white"
            if current_setup_node not in visited_nodes:
                color = "white"
            elif current_setup_node.data == "trap":
                color = "red"
            elif current_setup_node.data == "prize":
                color = "yellow"
            else:
                color = "gray"
            pygame.draw.circle(screen, color, pygame.Vector2(current_setup_node.x * square_size, current_setup_node.y * square_size), 10)
           
                    
        if player_position != last_player_position or starting == True:
            if starting == True:
                starting = False
            up_nodes = []
            down_nodes = []
            left_nodes = []
            right_nodes = []

            for child in lvl.edges[player_node_id]:
                if lvl.nodes[player_node_id].x < lvl.nodes[child].x:
                    left_nodes += [child]
                elif lvl.nodes[player_node_id].x > lvl.nodes[child].x:
                    right_nodes += [child]
                if lvl.nodes[player_node_id].y < lvl.nodes[child].y:
                    down_nodes += [child]
                elif lvl.nodes[player_node_id].y > lvl.nodes[child].y:
                    up_nodes += [child]
        
        # move player

        keys_pressed = pygame.key.get_pressed()
        selected_node = player_node
        # TODO: make code to move player
        pygame.draw.circle(screen, "green", player_position, 15)
        if keys_pressed[]
            
            # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

run_game()