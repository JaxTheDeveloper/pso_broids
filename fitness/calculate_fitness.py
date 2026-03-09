from vpython import *

def calculate_fitness(pos, target_pos, obstacles):
    # distance to target (minimize this)
    dist_to_target = mag(target_pos - pos) 
    
    # obstacle avoidance (apply massive penalty if too close)
    penalty = 0
    for obs in obstacles:
        # ignore y axis for distance calculation so cylinders act as infinite columns
        obs_center_xz = vec(obs.pos.x, 0, obs.pos.z)
        pos_xz = vec(pos.x, 0, pos.z)
        
        # avoid hitting walls
        if mag(pos_xz - obs_center_xz) < (obs.radius + 1.5): # buffer. maybe think of a inverse func for penalty
            print('huge penalty')
            penalty += (18*4)/(mag(pos_xz - obs_center_xz)) # typical cyllinder radius*4 as the constant

    # avoid phasing under the wall completely
    # i feel quite jolly, why not do a 
    # tiny dot product to extract the
    # y axis?
    if (dot(pos, vec(0, 1, 0)) < 0):
        penalty += float('inf')
            
    return dist_to_target + penalty