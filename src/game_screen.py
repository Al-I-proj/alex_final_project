import pygame
import math
import os

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


def level_screen(lvl: Graph, screen, square_size, visited_nodes, node_font, pixel_scale,
                 points_font, points):
    # draw the edges

    #DONE: add something to indicate directionality of edges
    #TODO: add something to indicate edge weights

    pixel_size = pixel_scale * 32
    completed_edges = {

    }
    for this_node_id in lvl.nodes_list:
        current_setup_node = lvl.nodes[this_node_id]
        current_setup_coordinates = pygame.Vector2((current_setup_node.x * square_size), (current_setup_node.y  * square_size))
        if this_node_id in lvl.edges:
            for child in lvl.edges[this_node_id]:
                already_visited = False
                if this_node_id in completed_edges:
                    if child in completed_edges[this_node_id]:
                        already_visited = True
                if not already_visited:
                    child_coordinates = pygame.Vector2(lvl.nodes[child].x * square_size, lvl.nodes[child].y * square_size)
                    if this_node_id in lvl.edges[child]:    
                        pygame.draw.line(screen, "white", 
                                        current_setup_coordinates,
                                        child_coordinates, 
                                        pixel_scale * 2)
                    else:
                        half_mark = ((child_coordinates - current_setup_coordinates)/2) + current_setup_coordinates
                        pygame.draw.line(screen, "white", 
                                        current_setup_coordinates,
                                        half_mark, 
                                        pixel_scale * 2)
                        pygame.draw.line(screen, "red", 
                                        half_mark,
                                        child_coordinates, 
                                        pixel_scale * 2)

                    if this_node_id in completed_edges:
                        completed_edges[this_node_id] += [child]
                    else:
                        completed_edges[this_node_id] = [child]
                    if child in completed_edges:
                        completed_edges[child] += [this_node_id]
                    else:
                        completed_edges[child] = [this_node_id]
                
                

    # draw the nodes and their text 
    for this_node_id in lvl.nodes_list:
        current_setup_node = lvl.nodes[this_node_id]
        current_setup_coordinates = pygame.Vector2(current_setup_node.x * square_size, current_setup_node.y * square_size)

        node_image_id = "src/assets/nodes/outlined_green_node.png"
        
        if current_setup_node.node_id in visited_nodes:

            text = node_font.render(str(current_setup_node.trap_distance), True, "red")
            backdrop = pygame.Rect((current_setup_coordinates[0] - (1.5 * text.get_size()[0]//2), 
                                   current_setup_coordinates[1] + (text.get_size()[1]//2) + (pixel_size * .25)),
                                    (text.get_size()[0] * 1.5, text.get_size()[1]))
            pygame.draw.rect(screen, "black", backdrop)
            screen.blit(text, 
                        pygame.Vector2(
                            current_setup_coordinates[0] - (text.get_size()[0]//2),
                            current_setup_coordinates[1] + (text.get_size()[1]//2) + (pixel_size * .25)
                        ))
            
            text = node_font.render(str(current_setup_node.prize_distance), True, "green")
            backdrop = pygame.Rect((current_setup_coordinates[0] - (1.5 * text.get_size()[0]//2), 
                                   current_setup_coordinates[1] - (text.get_size()[1]//2) - (pixel_size * .5)),
                                    (text.get_size()[0] * 1.5, text.get_size()[1]))
            pygame.draw.rect(screen, "black", backdrop)
            screen.blit(text, 
                        pygame.Vector2(
                            current_setup_coordinates[0] - (text.get_size()[0]//2),
                            current_setup_coordinates[1] - (text.get_size()[1]//2) - (pixel_size * .5)
                        ))

            if current_setup_node.data == "trap":
                node_image_id = "src/assets/nodes/outlined_red_node.png"
            elif current_setup_node.data == "prize":
                node_image_id = "src/assets/nodes/outlined_yellow_node.png"
            else:
                node_image_id = "src/assets/nodes/outlined_gray_node.png"
        # pygame.draw.circle(screen, color, 
        #                     current_setup_coordinates, 
        #                     pixel_scale)
        node_image = pygame.image.load(node_image_id)
        node_image = pygame.transform.scale(node_image, (node_image.get_size()[0] * pixel_scale, node_image.get_size()[1] * pixel_scale))
        screen.blit(node_image, current_setup_coordinates - pygame.Vector2(node_image.get_size()[0]//2, node_image.get_size()[1]//2))

        text = points_font.render(f"Found: {points} / {lvl.total_prizes}", True, "white")
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

def select_destination_node(lvl, left, right, up, down, player_node, selected_node):
    # a selection function for destination nodes
    
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
                return x_ordered[0][0]
            if len(x_ordered[1]) < 1:
                return selected_node
            return x_ordered[1][-1]
        
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

def display_player_node_data(lvl, player_node, screen, small_font):
    prize_info = small_font.render(f"nearest prize: {player_node.prize_distance}", True, "green")
    trap_info = small_font.render(f"nearest trap: {player_node.trap_distance}", True, "red")
    screen.blit(prize_info, pygame.Vector2(1000, 150 + (prize_info.get_size()[1])))
    screen.blit(trap_info, pygame.Vector2(1000, 150 + (trap_info.get_size()[1] * 2)))

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
    
def test_level(level_num):
    lvl = levels.make_level(level_num)

    run_game(lvl, level_num, level_num)

def set_up_animation(animation_directory_name):
    current_animation = []
    for frame in os.listdir(animation_directory_name):
        current_animation += [animation_directory_name + str(frame)]
    animation_frame_limit = len(current_animation)
    return (current_animation, animation_frame_limit)

    
def run_game(lvl = levels.level_1_graph(), lvl_counter = 1, final_level = 5, level_limit = 5):
    
    lvl.update_trap_and_prize_distances()
    
    if lvl.left > 1:
        rightmost = 0
        for node_id in lvl.nodes_list:
            lvl.nodes[node_id].x = lvl.nodes[node_id].x - lvl.left + 1
            lvl.nodes[node_id].coordinates = (lvl.nodes[node_id].x, lvl.nodes[node_id].y)
            if lvl.nodes[node_id].x > rightmost:
                rightmost = lvl.nodes[node_id].x
        lvl.left = 1
        lvl.right = rightmost

    if lvl.bottom > 1:
        topmost = 0
        for node_id in lvl.nodes_list:
            lvl.nodes[node_id].y = lvl.nodes[node_id].y - lvl.left + 1
            lvl.nodes[node_id].coordinates = (lvl.nodes[node_id].x, lvl.nodes[node_id].y)
            if lvl.nodes[node_id].y > topmost:
                topmost = lvl.nodes[node_id].y
        lvl.bottom = 1
        lvl.top = topmost

    if (lvl.top - lvl.bottom) * 16 > (lvl.right - lvl.left) * 9:
        lvl_scale = 1 / (1 + lvl.top - lvl.bottom)
    else:
        lvl_scale = 1 / (1 + lvl.right - lvl.left)

    pygame.init()
    #DONE: create system to display and interact with a graph

    #TODO: set up screen with consistant pixel style graphics
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    
    square_size = 640 * lvl_scale
    
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

    pixel_scale = round(12 * lvl_scale)
    player_size = 90 * lvl_scale

    selected_node = player_node
    current_position = pygame.Vector2(player_node.x, player_node.y)
    moving = False
    FPS_limit = 60

    animation_counter = 0
    animation_count_limit = FPS_limit//10
    move_counter = 0
    move_limit = FPS_limit//40
    travel_speed = 1/20
    
    sprite_animation_file = "src/assets/sprites/idle/"
    current_animation, animation_frame_limit = set_up_animation(sprite_animation_file)
    animation_frame = 0
    invert = False
    sprite_scale = pixel_scale

    selector_image = pygame.image.load("src/assets/selector_6.png")
    selector_image = pygame.transform.scale(selector_image, (selector_image.get_size()[0] * pixel_scale, 
                                                             selector_image.get_size()[1] * pixel_scale))

    death_animation = False
    testing = False
    level_to_test = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

        screen.fill("black")
        
        keys_pressed = pygame.key.get_pressed()
        
        # quit if escape key is pressed (to avoid issues if exit button is inaccessible)
        if not testing:
            if keys_pressed[pygame.K_ESCAPE]:
                running = False

        if game_over:
            game_over_screen(screen, title_font, points_font)
            
            if keys_pressed[pygame.K_SPACE]:
                visited_nodes = ["start"]
                player_node = lvl.nodes["start"]
                current_position = pygame.Vector2(player_node.x, player_node.y)
                selected_node = player_node
                points = 0
                prizes_found = 0
                game_over = False
                current_animation, animation_frame_limit = set_up_animation("src/assets/sprites/idle/")
                animation_frame = 0
        elif next_level:
            if final_level < lvl_counter:
                text = title_font.render("YOU WON!", True, "green")
                center = ((screen.get_size()[0]//2) - (text.get_size()[0]//2), screen.get_size()[1]//2 - (text.get_size()[1]//2))
                screen.blit(text, pygame.Vector2(center[0],center[1]))

            else:
                level_up_screen(screen, title_font, points_font)
                if keys_pressed[pygame.K_SPACE]:
                    lvl = levels.make_level(lvl_counter)
                    
                    lvl.update_trap_and_prize_distances()
                    visited_nodes = ["start"]
                    player_node = lvl.nodes["start"]
                    current_position = pygame.Vector2(player_node.x, player_node.y)
                    current_animation, animation_frame_limit = set_up_animation("src/assets/sprites/idle/")
                    animation_frame = 0
                    selected_node = player_node
                    points = 0
                    prizes_found = 0
                    next_level = False

        else:
            animation_counter += 1
            if animation_counter >= animation_count_limit:
                animation_frame += 1
                animation_frame = animation_frame % animation_frame_limit
                animation_counter = 0

            # pygame.draw.circle(screen, "purple", 
            #                    pygame.Vector2(selected_node.x * square_size, 
            #                                   selected_node.y * square_size),
            #                     player_size + 5)
            screen.blit(selector_image, 
                        pygame.Vector2((selected_node.x * square_size) - (selector_image.get_size()[0]//2), 
                                        (selected_node.y * square_size) - (selector_image.get_size()[1]//2)))
            level_screen(lvl, screen, square_size, visited_nodes, node_font, pixel_scale,
                         points_font, points)
            display_player_node_data(lvl, player_node, screen, points_font)
            
            # move player

            # DONE: make code to move player in cardinal directions
            # DONE: make code to move the player diagonally
            sprite_image = pygame.image.load(current_animation[animation_frame])
            sprite_image = pygame.transform.scale(sprite_image, (sprite_image.get_size()[0] * sprite_scale, sprite_image.get_size()[1] * sprite_scale))
            
            if invert:
                sprite_image = pygame.transform.flip(sprite_image, True, False)
            screen.blit(sprite_image, (current_position * square_size) - (pygame.Vector2(sprite_image.get_size()[0], sprite_image.get_size()[1])//2))

            if not death_animation:
                left, right, down, up = (False, False, False, False)
                if new_key_lift(pygame.K_a, last_key_positions, keys_pressed):
                    left = True
                if new_key_lift(pygame.K_d, last_key_positions, keys_pressed):
                    right = True
                if new_key_lift(pygame.K_w, last_key_positions, keys_pressed):
                    up = True
                if new_key_lift(pygame.K_s, last_key_positions, keys_pressed):
                    down = True

                #testing cheat setup to skip to specific levels
                if keys_pressed[pygame.K_l] and keys_pressed[pygame.K_v] and keys_pressed[pygame.K_t]:
                    testing = True
                if testing:
                    text = points_font.render(f"test level: {level_to_test}", True, "white", "black")
                    screen.blit(text, (10,10))
                    if new_key_lift(pygame.K_BACKSPACE, last_key_positions, keys_pressed):
                        if len(level_to_test) > 0:
                            level_to_test = level_to_test[:-1]
                    if new_key_lift(pygame.K_0, last_key_positions, keys_pressed):
                        level_to_test += "0"
                    elif new_key_lift(pygame.K_1, last_key_positions, keys_pressed):
                        level_to_test += "1"
                    elif new_key_lift(pygame.K_2, last_key_positions, keys_pressed):
                        level_to_test += "2"
                    elif new_key_lift(pygame.K_3, last_key_positions, keys_pressed):
                        level_to_test += "3"
                    elif new_key_lift(pygame.K_4, last_key_positions, keys_pressed):
                        level_to_test += "4"
                    elif new_key_lift(pygame.K_5, last_key_positions, keys_pressed):
                        level_to_test += "5"
                    elif new_key_lift(pygame.K_6, last_key_positions, keys_pressed):
                        level_to_test += "6"
                    elif new_key_lift(pygame.K_7, last_key_positions, keys_pressed):
                        level_to_test += "7"
                    elif new_key_lift(pygame.K_8, last_key_positions, keys_pressed):
                        level_to_test += "8"
                    elif new_key_lift(pygame.K_9, last_key_positions, keys_pressed):
                        level_to_test += "9"
                    
                    if new_key_lift(pygame.K_RETURN, last_key_positions, keys_pressed):
                        if len(level_to_test) > 0:
                            level_to_test = int(level_to_test)
                        else:
                            level_to_test = lvl_counter
                        
                        if level_to_test > level_limit:
                            level_to_test = lvl_counter

                        test_level(level_to_test)
                        running = False

                    if new_key_lift(pygame.K_ESCAPE, last_key_positions, keys_pressed):
                        testing = False
                        level_to_test = ""
                    
                    
                if not moving:  
                    destination_node = player_node
                    if player_node.node_id in lvl.edges:
                        selected_node = select_destination_node(lvl, left, right, up, down, player_node, selected_node)
                        if new_key_lift(pygame.K_SPACE, last_key_positions, keys_pressed):
                            destination_node = selected_node
                #DONE: Make sprite animation code
                #DONE: Make code to smoothly move sprite

                if destination_node != player_node:
                    moving = True
                    direction = pygame.Vector2((destination_node.x - player_node.x) , 
                                                (destination_node.y -  player_node.y))
                    invert = False
                    if direction.x != 0:
                        sprite_animation_file = "src/assets/sprites/D_walk/"
                        if direction.x < 0:
                            invert = True
                    if direction.y > 0 and abs(direction.y) > abs(direction.x):
                        sprite_animation_file = "src/assets/sprites/S_walk/"
                    if direction.y < 0 and abs(direction.y) > abs(direction.x):
                        sprite_animation_file = "src/assets/sprites/W_walk/"
                    

                    current_animation = []
                    animation_frame = 0
                    current_animation, animation_frame_limit = set_up_animation(sprite_animation_file)
                
                if moving == True:
                    move_counter += 1
                    if move_counter >= move_limit:
                        move_counter = 0
                            
                        if (direction[0] * direction[0]) + (direction[1] * direction[1]) == 0:
                            direction_unit = pygame.Vector2(.1,.1)
                        else:
                            direction_unit = (direction / math.sqrt((direction[0] * direction[0]) + (direction[1] * direction[1]))
                                            ) * travel_speed
                        next_position = current_position + direction_unit
                        traveled_distance = (current_position[0] - player_node.x, current_position[1] - player_node.y)
                        if (abs(traveled_distance[0]) < abs(direction[0] - direction_unit[0]) or 
                            abs(traveled_distance[1]) < abs(direction[1] - direction_unit[1])):
                                current_position = next_position
                        else:
                            player_node = destination_node
                            current_position = pygame.Vector2(player_node.x, player_node.y)
                            moving = False
                            sprite_animation_file = "src/assets/sprites/idle/"
                            animation_frame = 0
                            current_animation, animation_frame_limit = set_up_animation(sprite_animation_file)


                        if not moving:
                            if destination_node.node_id not in visited_nodes:
                                visited_nodes += [destination_node.node_id]
                                if destination_node.data == "prize":
                                    points += 1
                                    prizes_found += 1
                                    if prizes_found == total_prizes:
                                        next_level = True
                                        lvl_counter += 1
                                    current_animation, animation_frame_limit = set_up_animation("src/assets/sprites/prize_sprite/")
                                elif destination_node.data == "trap":
                                    death_animation = True
                                    current_animation, animation_frame_limit = set_up_animation("src/assets/sprites/trap/")
                                    animation_frame = 0
                                    #game_over = True
                last_key_positions = keys_pressed
            elif animation_frame == animation_frame_limit - 1:
                game_over = True
                death_animation = False

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(FPS_limit)  # limits FPS to 60

    pygame.quit()

run_game()
#test_level(6)