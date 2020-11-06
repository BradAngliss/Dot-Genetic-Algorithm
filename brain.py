import random
import math

class Brain:
    def __init__(self, size):
        self.size = size
        self.step = 0
        self.directions = []
        self.randomise()

    def vectFromRadians(self, angle):
        return [math.cos(angle), math.sin(angle)]

    def randomise(self):
        for i in range(self.size):
            randomAngle = random.uniform(0, 2*math.pi)
            vector = self.vectFromRadians(randomAngle)
            self.directions.append(vector)

    def cloneBrain(self):
        newBrain = Brain(len(self.directions))
        newBrain.directions = self.directions.copy()
        return newBrain

    def mutate(self):
        mutationRate = 0.01
        for i in range(len(self.directions)):
            rand = random.uniform(0, 1)
            print(rand)
            if (rand < mutationRate):
                randomAngle = random.uniform(0, 2*math.pi)
                self.directions[i] = self.vectFromRadians(randomAngle)