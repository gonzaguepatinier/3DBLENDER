from pyramid import Pyramid
from stone import Stone
from stone import StoneQuality


def main_build():
    my_pyramid = Pyramid(7)
    my_pyramid.display_pyramid()

    stone1 = Stone()
    stone1.quarry_stone(quality=StoneQuality.HIGH, number = 1)
    
    stone2 = Stone()
    stone2.quarry_stone(quality=StoneQuality.LOW, number = 1)

    my_pyramid.lay_stone(stone1, layer_number = 1, x = 2, y = 2)
    my_pyramid.lay_stone(stone2, layer_number = 1, x = 1, y = 1)
    # my_pyramid.display_pyramid()
    my_pyramid.display_pyramid_layer(1)


    return

if __name__ == "__main__":
    print('run as script')
    main_build()
else:
    print('starting addon')
    main_build()