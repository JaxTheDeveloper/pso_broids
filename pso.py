from vpython import *
import random

# import scene objects
from scene_objects.cyllinder import create_retro_pillar
from scene_objects.gridTile import create_tile_grid

# import particle objects
from particle.particle import Particle

# import fitness function
from fitness.calculate_fitness import calculate_fitness

# scene setup
scene = canvas(title='PSO Boid Navigation', width=800, height=600, background=color.white)

create_tile_grid(size=80, tile_size=10, y_level=-5)

start_pos = vec(-25, 0, 0)
target_pos = vec(25, 0, 0)

sphere(pos=start_pos, radius=1, color=color.blue, opacity=0.5)   # Start
sphere(pos=target_pos, radius=1, color=color.green, opacity=0.5) # Target

# create the obstacles using the pillar ngon function
obstacles = [
    create_retro_pillar(vec(-10, -5, 5), radius=3, height=10, sides=12),
    create_retro_pillar(vec(0, -5, -5), radius=3, height=10, sides=12),
    create_retro_pillar(vec(10, -5, 5), radius=3, height=10, sides=12)
]

# swarm
possible_start_pos = [start_pos, vec(-25, 0, -25), vec(-25, 0, 25)]

num_particles = 30
swarm = [Particle(possible_start_pos=possible_start_pos) for _ in range(num_particles)]
gBest = start_pos
gBest_fitness = float('inf')

# pso params
c1 = 2 # cognitive (personal best) weight
c2 = 3.5 # social (global best) weight
max_speed = 0.65 # To prevent them from jumping through walls

# pso
while True:
    rate(144) # Limits loop to 60 frames per second
    
    # evaluate fitness and update pbest, gbest
    for a in swarm:
        a.fp = calculate_fitness(a.Pos, target_pos, obstacles)
        
        # pbest
        if a.fp < calculate_fitness(a.pBest, target_pos, obstacles):
            a.pBest = vec(a.Pos.x, a.Pos.y, a.Pos.z) # copy vector
            
        # gbest
        if a.fp < gBest_fitness:
            gBest_fitness = a.fp
            gBest = vec(a.Pos.x, a.Pos.y, a.Pos.z)

    # velocity and pos
    for a in swarm:
        rand1 = random.random()
        rand2 = random.random()
        
        # same math stuff
        cognitive_pull = c1 * rand1 * (a.pBest - a.Pos)
        social_pull = c2 * rand2 * (gBest - a.Pos)
        
        a.Vel = a.Vel + cognitive_pull + social_pull
        
        # limit speed so boids don't break the physics simulation
        # say, they go so fast that the next update cycle they phased through a wall (or inside one of them)
        if mag(a.Vel) > max_speed:
            a.Vel = norm(a.Vel) * max_speed # normalizes vector to length 1, this makes them exceedingly slow
            
        a.Pos = a.Pos + a.Vel
        
        # update 3D visualization
        a.boid.pos = a.Pos
        a.boid.axis = a.Vel # makes the cone point in the direction it is moving