import pygame

from graph import Graph, Node
import levels

def new_key_press(key, last_key_positions, keys_pressed):
    if last_key_positions[key] != keys_pressed[key] and keys_pressed[key]:
        return True
    return False

def run_game():
    lvl = levels.level_1_graph()
    lvl_counter = 1
    max_levels = 2

    pygame.init()
    #TODO: create system to display and interact with a graph

    screen = pygame.display.set_mode((1280, 720))
    square_size = 100
    clock = pygame.time.Clock()
    running = True
    
    visited_nodes = ["start"]
    player_node = lvl.nodes["start"]

    starting = True
    last_key_positions = pygame.key.get_pressed()

    node_font = pygame.font.SysFont("georgia", 20)

    points_font = pygame.font.SysFont("georgia", 24)
    points = 0

    prizes_found = 0
    total_prizes = lvl.total_prizes

    title_font = pygame.font.SysFont("georgia", 48)
    game_over = False
    next_level = False

    node_size = 10
    player_size = 15

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

        # RENDER YOUR GAME HERE
        screen.fill("black")
        if game_over:
            text = title_font.render("GAME OVER", True, "red")
            center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
            screen.blit(text, pygame.Vector2(center[0],center[1] - 50))
            text = title_font.render("PLAY AGAIN?", True, "white")
            center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
            screen.blit(text, pygame.Vector2(center[0],center[1] + 50))
            text = points_font.render("(press space)", True, "white")
            center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
            screen.blit(text, pygame.Vector2(center[0], center[1] + 100))
            
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                visited_nodes = ["start"]
                player_node = lvl.nodes["start"]
                points = 0
                game_over = False
        elif next_level:
            text = title_font.render("LEVEL UP!", True, "green")
            center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
            screen.blit(text, pygame.Vector2(center[0],center[1] - 50))
            text = points_font.render("(press space to continue)", True, "white")
            center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
            screen.blit(text, pygame.Vector2(center[0], center[1] + 50))
            
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                if lvl_counter == 2:
                    lvl = levels.level_2_graph() 
                visited_nodes = ["start"]
                player_node = lvl.nodes["start"]
                points = 0

        else:
            # draw the edges
            for this_node_id in lvl.nodes_list:
                current_setup_node = lvl.nodes[this_node_id]
                if this_node_id in lvl.edges:
                    for child in lvl.edges[this_node_id]:
                        pygame.draw.line(screen, "white", 
                                        pygame.Vector2(current_setup_node.x * square_size, current_setup_node.y  * square_size),
                                        pygame.Vector2(lvl.nodes[child].x * square_size, lvl.nodes[child].y * square_size), 
                                        5)

            # draw the nodes and their text 
            for this_node_id in lvl.nodes_list:
                current_setup_node = lvl.nodes[this_node_id]
                color = "white"
                if current_setup_node.node_id not in visited_nodes:
                    color = "white"
                else:
                    text = node_font.render(str(current_setup_node.trap_distance), True, "red")
                    screen.blit(text, 
                                pygame.Vector2(
                                    (current_setup_node.x * square_size) - (text.get_size()[0]//2),
                                    (current_setup_node.y * square_size) + (text.get_size()[1]//2) + (node_size)
                                ))
                    text = node_font.render(str(current_setup_node.prize_distance), True, "green")
                    screen.blit(text, 
                                pygame.Vector2(
                                    (current_setup_node.x * square_size) - (text.get_size()[0]//2),
                                    (current_setup_node.y * square_size) - (text.get_size()[1]//2) - (node_size * 4)
                                ))

                    if current_setup_node.data == "trap":
                        color = "red"
                    elif current_setup_node.data == "prize":
                        color = "green"
                    else:
                        color = "gray"
                pygame.draw.circle(screen, color, 
                                   pygame.Vector2(current_setup_node.x * square_size, current_setup_node.y * square_size), 
                                   node_size)

            text = points_font.render(f"Points: {points}", True, "white")
            screen.blit(text, pygame.Vector2(1000,100))
            # move player

            keys_pressed = pygame.key.get_pressed()
            player_position = pygame.Vector2(player_node.x * square_size, player_node.y * square_size)
            # DONE: make code to move player in cardinal directions
            # TODO: make code to move the player diagonally
            pygame.draw.circle(screen, "yellow", player_position, player_size)
            left, right, down, up = (False, False, False, False)
            if new_key_press(pygame.K_a, last_key_positions, keys_pressed):
                left = True
            if new_key_press(pygame.K_d, last_key_positions, keys_pressed):
                right = True
            if new_key_press(pygame.K_w, last_key_positions, keys_pressed):
                up = True
            if new_key_press(pygame.K_s, last_key_positions, keys_pressed):
                down = True
            
            destination_node = player_node
            if player_node.node_id in lvl.edges:
                if left and not right:
                    #max_distance = 0
                    for possible_node in lvl.edges[player_node.node_id]:
                        if lvl.nodes[possible_node].x < player_node.x:
                            destination_node = lvl.nodes[possible_node]
                            #max_distance = player_node.x - lvl.nodes[possible_node].x
                elif right and not left:
                    for possible_node in lvl.edges[player_node.node_id]:
                        if lvl.nodes[possible_node].x > player_node.x:
                            destination_node = lvl.nodes[possible_node]
                elif up and not down:
                    for possible_node in lvl.edges[player_node.node_id]:
                        if lvl.nodes[possible_node].y > player_node.y:
                            destination_node = lvl.nodes[possible_node]
                elif down and not up:
                    for possible_node in lvl.edges[player_node.node_id]:
                        if lvl.nodes[possible_node].y < player_node.y:
                            destination_node = lvl.nodes[possible_node]

            if destination_node != player_node:
                if destination_node.node_id not in visited_nodes:
                    visited_nodes += [destination_node.node_id]
                    if destination_node.data == "prize":
                        points += 10
                        prizes_found += 1
                        if prizes_found == total_prizes:
                            next_level = True
                            lvl_counter += 1
                    elif destination_node.data == "trap":
                        game_over = True
                player_node = destination_node
                pygame.draw.circle(screen, "yellow", player_position, 15)



            last_key_positions = keys_pressed
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

run_game()