from pyramid import Pyramid
from stone import Stone
from stone import quarry_stone
from stone import StoneQuality
import bpy

# To run in VSCODE
# Command + Shift + P
# Blender: Start
# 
# Add module here:
# /Applications/Blender.app/Contents/Resources/3.6/scripts/modules

def main_build():
    my_pyramid = Pyramid(7)
    my_pyramid.display_pyramid()

    stone1 = quarry_stone(quality=StoneQuality.HIGH, number = 1)
    stone2 = quarry_stone(quality=StoneQuality.LOW, number = 1)
    stone3 = quarry_stone(quality=StoneQuality.LOW, number = 1)

    my_pyramid.lay_stone(stone1, layer_number = 1, x = 1, y = 1)
    my_pyramid.lay_stone(stone2, layer_number = 1, x = 1, y = 2)
    my_pyramid.lay_stone(stone3, layer_number = 1, x = 1, y = 3)
    # my_pyramid.display_pyramid()
    # my_pyramid.display_pyramid_layer(1)

    my_pyramid.display3d_pyramid()

    # bpy.ops.mesh.primitive_cube_add(location=(1,1,1))

    return

if __name__ == "__main__":
    print('run as script')
    main_build()
else:
    print('starting addon')
    main_build()