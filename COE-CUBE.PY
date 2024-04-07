import bpy
from random import randint
# bpy.ops.mesh.primitive_cube_add()
# How to run script


# count = 5
# for c in range(0,count):
#     x = randint(-10,10)
#     y = randint(-10,10)
#     z = randint(-10,10)
#     bpy.ops.mesh.primitive_cube_add(location=(x,y,z))

def main_blender():
    count = 5
    for c in range(0,count):
        x = randint(-10,10)
        y = randint(-10,10)
        z = randint(-10,10)
        bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
#how many cubes you want to add


if __name__ == "__main__":
    print('run as script')
else:
    print('starting addon')
    main_blender()
