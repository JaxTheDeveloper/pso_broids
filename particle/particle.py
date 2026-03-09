from vpython import *
import random

class Particle:
    def __init__(self, possible_start_pos):
        # initialize near start position with slight randomness

        # choose a spawn position candidate
        candidate_start_pos = possible_start_pos[random.randrange(len(possible_start_pos))]

        self.Pos = candidate_start_pos + vec(random.uniform(-4,4), random.uniform(-4,4), random.uniform(-4,4))
        self.Vel = vec(random.uniform(-2,2), random.uniform(-2,2), random.uniform(-2,2))
        
        self.pBest = self.Pos
        self.fp = float('inf') # fitness score. everyone shares a terrible fitness
        
        # visual representation: Cone shaped, pointing in the direction of velocity
        self.boid = cone(pos=self.Pos, axis=self.Vel, radius=0.5, length=1.5, color=color.black, opacity=0.3, emission=True)