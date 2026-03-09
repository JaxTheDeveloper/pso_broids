from vpython import *

def create_retro_pillar(base_pos, radius, height, sides=12):
    # create a polygon
    poly_shape = shapes.ngon(np=sides, length=radius)
    core = extrusion(path=[base_pos, base_pos + vec(0, height, 0)], 
                     shape=poly_shape, color=color.white, emissive=True)
    
    # fraw the black wireframe lines
    vertices = []
    for i in range(sides):
        angle = i * (2 * pi / sides)
        x = radius * cos(angle)
        z = radius * sin(angle)
        vertices.append(vec(base_pos.x + x, base_pos.y, base_pos.z + z))
        
    # draw bottom ring
    bottom_pts = vertices + [vertices[0]] 
    curve(pos=bottom_pts, color=color.black, radius=0.05)
    
    # fraw top ring
    top_pts = [v + vec(0, height, 0) for v in bottom_pts]
    curve(pos=top_pts, color=color.black, radius=0.05)
    
    # draw vertical edges connecting the rings
    for i in range(sides):
        curve(pos=[vertices[i], vertices[i] + vec(0, height, 0)], color=color.black, radius=0.05)
        
    # return data to reliably calculate collisions
    class ObstacleData:
        def __init__(self, p, r):
            self.pos = p
            self.radius = r
    return ObstacleData(base_pos, radius)