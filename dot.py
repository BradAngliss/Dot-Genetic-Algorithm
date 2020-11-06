from coords import Position
from brain import Brain

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Dot:
    def __init__(self, windowWidth, windowHeight):
        self.brain = Brain(1000)

        # Starting location at the bottom center with no velocity or acceleration
        self.pos = Position(windowWidth // 2, windowHeight - 10)
        self.vel = Position(0, 0)
        self.acc = Position(0, 0)

        self.dead = False
        self.reachedGoal = False
        self.isBest = False

        self.fitness = 0

    def show():
        if (isBest):
            pygame.draw.circle(screen, GREEN, (self.pos.x, self.pos.y), 6)
        else:
            pygame.draw.circle(screen, BLACK, (self.pos.x, self.pos.y), 4)
