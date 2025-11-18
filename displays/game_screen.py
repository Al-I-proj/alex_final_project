import pygame

from src.graph import Graph, Node
def level_1_graph():
    #TODO: create a level and create a structure by which coordinates can be manually assigned to the nodes
    pass


def run_game():
    lvl_1 = level_1_graph()

    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()