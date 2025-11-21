import pygame
import math

from graph import Graph, Node
import levels

def new_key_press(key, last_key_positions, keys_pressed):
    if last_key_positions[key] != keys_pressed[key] and keys_pressed[key]:
        return True
    return False

def new_key_lift(key, last_key_positions, keys_pressed):
    if last_key_positions[key] != keys_pressed[key] and not keys_pressed[key]:
        return True
    return False


def level_screen(lvl: Graph, screen, square_size, visited_nodes, node_font, node_size,
                 points_font, points):
    # draw the edges

    for this_node_id in lvl.nodes_list:
        current_setup_node = lvl.nodes[this_node_id]
        current_setup_coordinates = pygame.Vector2(current_setup_node.x * square_size, current_setup_node.y  * square_size)
        if this_node_id in lvl.edges:
            for child in lvl.edges[this_node_id]:
                child_coordinates = pygame.Vector2(lvl.nodes[child].x * square_size, lvl.nodes[child].y * square_size)
                pygame.draw.line(screen, "white", 
                                current_setup_coordinates,
                                child_coordinates, 
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

def game_over_screen(screen, title_font, points_font):
    text = title_font.render("GAME OVER", True, "red")
    center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
    screen.blit(text, pygame.Vector2(center[0],center[1] - 50))
    text = title_font.render("PLAY AGAIN?", True, "white")
    center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
    screen.blit(text, pygame.Vector2(center[0],center[1] + 50))
    text = points_font.render("(press space)", True, "white")
    center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
    screen.blit(text, pygame.Vector2(center[0], center[1] + 100))

def level_up_screen(screen, title_font, points_font):
    text = title_font.render("LEVEL UP!", True, "green")
    center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
    screen.blit(text, pygame.Vector2(center[0],center[1] - 50))
    text = points_font.render("(press space to continue)", True, "white")
    center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
    screen.blit(text, pygame.Vector2(center[0], center[1] + 50))
    
def find_destination_node(lvl, left, right, up, down, player_node):
    # factors used to compare with less repetatitive code using greater than comparissons

    x_factor, y_factor = (0, 0)
    if left and not right:
        x_factor = 1
    elif right and not left:
        x_factor = -1
    if down and not up:
        y_factor = -1
    elif up and not down:
        y_factor = 1
    
    destination_node = player_node
    for possible_node in lvl.edges[player_node.node_id]:
        if y_factor == 0:    
            if (lvl.nodes[possible_node].x * x_factor < player_node.x * x_factor
                and lvl.nodes[possible_node].y == player_node.y):
                destination_node = lvl.nodes[possible_node]
        elif x_factor == 0:    
            if (lvl.nodes[possible_node].y * y_factor < player_node.y * y_factor
                and lvl.nodes[possible_node].x == player_node.x):
                destination_node = lvl.nodes[possible_node]
        else:
            if (lvl.nodes[possible_node].x * x_factor < player_node.x * x_factor 
                and lvl.nodes[possible_node].y * y_factor < player_node.y * y_factor ):
                destination_node = lvl.nodes[possible_node]
    return destination_node


def select_destination_node(lvl, left, right, up, down, player_node, selected_node):
    # a possible selection method for destination nodes on more complex graphs

    #TODO: fix selection glitch for diagonal edges which end at the same x/y but not the same y/x
    #   currently the program sometimes fails to ever reach one of the nodes
    if left != right or up != down:
        x_ordered = [[],[]]
        y_ordered = [[],[]]
        
        if player_node.node_id in lvl.edges:
            for neighbor in lvl.edges[player_node.node_id]:
                if selected_node.x > lvl.nodes[neighbor].x:
                    x_ordered[0] += [lvl.nodes[neighbor]]
                elif selected_node.x < lvl.nodes[neighbor].x:
                    x_ordered[1] += [lvl.nodes[neighbor]]
                if selected_node.y > lvl.nodes[neighbor].y:
                    y_ordered[0] += [lvl.nodes[neighbor]]
                elif selected_node.y < lvl.nodes[neighbor].y:
                    y_ordered[1] += [lvl.nodes[neighbor]]
        x_ordered[0] = quick_sort(x_ordered[0], by_x = True)
        x_ordered[1] = quick_sort(x_ordered[1], by_x = True)
        y_ordered[0] = quick_sort(y_ordered[0], by_y = True)
        y_ordered[1] = quick_sort(y_ordered[1], by_y = True)
        if left or right and left != right:
            if left:
                if len(x_ordered[0]) < 1:
                    return selected_node
                return x_ordered[0][-1]
            if len(x_ordered[1]) < 1:
                return selected_node
            return x_ordered[1][0]
        
        if up or down and up != down:
            
            if up:
                if len(y_ordered[0]) < 1:
                    return selected_node
                return y_ordered[0][-1]
            if len(y_ordered[1]) < 1:
                return selected_node
            return y_ordered[1][0]
        
        return selected_node
    else:
        return selected_node

def quick_sort(unordered_list: list, by_x = False, by_y = False):
    if len(unordered_list) <= 1:
        return unordered_list
    
    more = []
    less = []
    pivot = unordered_list[0]
    
    for entry in unordered_list[1:]:
        if by_x:
            if pivot.x < entry.x:
                more += [entry]
            elif pivot.x == entry.x:
                if pivot.y > entry.y:
                    more += [entry]
                else:
                    less += [entry]
            else:
                less += [entry]
        elif by_y:
            if pivot.y < entry.y:
                more += [entry]
            elif pivot.y == entry.y:
                if pivot.x > entry.x:
                    more += [entry]
                else:
                    less += [entry]
            else:
                less += [entry]
        else:
            if pivot < entry:
                more += [entry]
            else:
                less += [entry]
    return quick_sort(less, by_x, by_y) + [pivot] + quick_sort(more, by_x, by_y)
    



        

    
def run_game():
    lvl = levels.level_1_graph()
    lvl_counter = 1
    max_levels = 2

    pygame.init()
    #DONE: create system to display and interact with a graph

    screen = pygame.display.set_mode((1280, 720))
    square_size = 100
    clock = pygame.time.Clock()
    running = True
    
    visited_nodes = ["start"]
    player_node = lvl.nodes["start"]

    last_key_positions = pygame.key.get_pressed()

    node_font = pygame.font.SysFont("georgia", 20)

    points_font = pygame.font.SysFont("georgia", 24)
    points = 0

    prizes_found = 0
    total_prizes = lvl.total_prizes

    title_font = pygame.font.SysFont("georgia", 48)
    game_over = False
    next_level = False
    starting = True

    node_size = 10
    player_size = 15

    selected_node = player_node

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

        # RENDER YOUR GAME HERE
        screen.fill("black")
        if game_over:
            game_over_screen(screen, title_font, points_font)
            
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                visited_nodes = ["start"]
                player_node = lvl.nodes["start"]
                selected_node = player_node
                points = 0
                prizes_found = 0
                game_over = False
        elif next_level:
            if max_levels < lvl_counter:
                text = title_font.render("YOU WON!", True, "green")
                center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
                screen.blit(text, pygame.Vector2(center[0],center[1]))

            else:
                level_up_screen(screen, title_font, points_font)
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_SPACE]:
                    if lvl_counter == 2:
                        lvl = levels.level_2_graph()
                    
                    lvl.update_trap_and_prize_distances()
                    visited_nodes = ["start"]
                    player_node = lvl.nodes["start"]
                    selected_node = player_node
                    points = 0
                    prizes_found = 0
                    next_level = False

        else:
            pygame.draw.circle(screen, "purple", 
                               pygame.Vector2(selected_node.x * square_size, 
                                              selected_node.y * square_size),
                                player_size + 5)
            level_screen(lvl, screen, square_size, visited_nodes, node_font, node_size,
                         points_font, points)
            # move player


            keys_pressed = pygame.key.get_pressed()
            player_position = pygame.Vector2(player_node.x * square_size, player_node.y * square_size)
            # DONE: make code to move player in cardinal directions
            # TODO: make code to move the player diagonally
            pygame.draw.circle(screen, "yellow", player_position, player_size)
            left, right, down, up = (False, False, False, False)
            if new_key_lift(pygame.K_a, last_key_positions, keys_pressed):
                left = True
            if new_key_lift(pygame.K_d, last_key_positions, keys_pressed):
                right = True
            if new_key_lift(pygame.K_w, last_key_positions, keys_pressed):
                up = True
            if new_key_lift(pygame.K_s, last_key_positions, keys_pressed):
                down = True
                    
            destination_node = player_node
            if player_node.node_id in lvl.edges:
                # if left and not right:
                #     #max_distance = 0
                #         for possible_node in lvl.edges[player_node.node_id]:
                #             if lvl.nodes[possible_node].x < player_node.x:
                #                 destination_node = lvl.nodes[possible_node]
                #                 #max_distance = player_node.x - lvl.nodes[possible_node].x
                # elif right and not left:
                #     for possible_node in lvl.edges[player_node.node_id]:
                #         if lvl.nodes[possible_node].x > player_node.x:
                #             destination_node = lvl.nodes[possible_node]
                # elif up and not down:
                #     for possible_node in lvl.edges[player_node.node_id]:
                #         if lvl.nodes[possible_node].y > player_node.y:
                #             destination_node = lvl.nodes[possible_node]
                # elif down and not up:
                #     for possible_node in lvl.edges[player_node.node_id]:
                #         if lvl.nodes[possible_node].y < player_node.y:
                #             destination_node = lvl.nodes[possible_node]


                #destination_node = find_destination_node(lvl, left, right, up ,down, player_node)
                selected_node = select_destination_node(lvl, left, right, up, down, player_node, selected_node)
                if new_key_lift(pygame.K_SPACE, last_key_positions, keys_pressed):
                    destination_node = selected_node

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