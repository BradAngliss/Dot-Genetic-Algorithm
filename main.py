import pygame
import os

from coords import Position
from dot import Dot
RED = (255, 0, 0)

def main():
    fps_lim = 60
    running = True

    width = 800
    height = 800

    # Assigning the coordinates of the goal 10% from the top and halfway horizontally
    goal = Position(width // 2, int(height * 0.1))

    # Setup pygame initialisation parameters
    pygame.init()
    pygame.display.set_caption("Dot Genetic Algorithm")

    screen = pygame.display.set_mode((width, height))
    screen.fill((255, 255, 255))

    clock = pygame.time.Clock()



    d = Dot()    
    # print(d.brain.directions)
    d.brain.mutate()
    # print(d.brain.directions)

    while(running):
        clock.tick(fps_lim)

        pygame.display.flip()

        # Draw goal
        pygame.draw.circle(screen, RED, (goal.x, goal.y), 8)

        # Draw obstacle

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()