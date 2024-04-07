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
    my_pyramid = Pyramid(3)
    my_pyramid.display_pyramid()

# TODO: Add a stock clas?
# TODO: Pull Stone from stock
# TODO: Load Pyramid design from XLS File

    stone1 = quarry_stone(quality=StoneQuality.HIGH, number = 1)
    stone2 = quarry_stone(quality=StoneQuality.LOW, number = 2)
    stone3 = quarry_stone(quality=StoneQuality.LOW, number = 3)
    stone4 = quarry_stone(quality=StoneQuality.LOW, number = 4)
    stone5 = quarry_stone(quality=StoneQuality.LOW, number = 5)
    stone6 = quarry_stone(quality=StoneQuality.LOW, number = 6)
    stone7 = quarry_stone(quality=StoneQuality.LOW, number = 7)
    stone8 = quarry_stone(quality=StoneQuality.LOW, number = 7)
    stone9 = quarry_stone(quality=StoneQuality.LOW, number = 7)
    stone10 = quarry_stone(quality=StoneQuality.LOW, number = 7)
    stone11 = quarry_stone(quality=StoneQuality.LOW, number = 7)
    stone12 = quarry_stone(quality=StoneQuality.LOW, number = 7)
    stone13 = quarry_stone(quality=StoneQuality.LOW, number = 7)

    my_pyramid.lay_stone(stone1, layer_number = 1, x = 1, y = 1)
    my_pyramid.lay_stone(stone2, layer_number = 1, x = 2, y = 1)
    my_pyramid.lay_stone(stone3, layer_number = 1, x = 3, y = 1)

    my_pyramid.lay_stone(stone4, layer_number = 1, x = 1, y = 2)
    my_pyramid.lay_stone(stone5, layer_number = 1, x = 3, y = 2)

    my_pyramid.lay_stone(stone6, layer_number = 1, x = 1, y = 3)
    my_pyramid.lay_stone(stone7, layer_number = 1, x = 2, y = 3)
    my_pyramid.lay_stone(stone8, layer_number = 1, x = 3, y = 3)

    my_pyramid.lay_stone(stone9, layer_number = 2, x = 1, y = 1)
    my_pyramid.lay_stone(stone10, layer_number = 2, x = 1, y = 2)
    my_pyramid.lay_stone(stone11, layer_number = 2, x = 2, y = 1)
    my_pyramid.lay_stone(stone12, layer_number = 2, x = 2, y = 2)

    my_pyramid.lay_stone(stone13, layer_number = 3, x = 1, y = 1)
    
    my_pyramid.display_pyramid()
    my_pyramid.display_pyramid_layer(1)
    my_pyramid.display_pyramid_layer(2)

    my_pyramid.display3d_pyramid()

    # bpy.ops.mesh.primitive_cube_add(location=(1,1,1))

    return

if __name__ == "__main__":
    print('run as script')
    main_build()
else:
    print('starting addon')
    main_build()