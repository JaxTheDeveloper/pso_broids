from vpython import *

def create_tile_grid(size=60, tile_size=10, y_level=-5):
    # 'size' is the total width/length of the grid
    # 'tile_size' is how big each square tile is
    
    half_size = size // 2
    
    # draw lines parallel to the z axis
    for x in range(-half_size, half_size + 1, tile_size):
        curve(pos=[vec(x, y_level, -half_size), vec(x, y_level, half_size)], 
              color=color.black, radius=0.05)
        
    # draw lines parallel to the z axis
    for z in range(-half_size, half_size + 1, tile_size):
        curve(pos=[vec(-half_size, y_level, z), vec(half_size, y_level, z)], 
              color=color.black, radius=0.05)