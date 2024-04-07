from dataclasses import dataclass
from typing import List
from stone import Stone
from layer import Layer
@dataclass
class Pyramid:
    layer: List[Layer]
    layer_number: int

    def __init__(self, layer_number: int):
        self.layer_number = layer_number
        self.layer = []
        for layer_index in range(1, layer_number+1):
            self.layer.append(Layer(layer_number = layer_index, 
                                    grid_size = (layer_number + 1 - layer_index)))
            
    def display_pyramid(self) -> None:
        for layer in self.layer:
            layer.display_layer()
    
    def display3d_pyramid(self) -> None:
        for layer in self.layer:
            layer.display3d_layer()

    def display_pyramid_layer(self, layer_number: int) -> None:
            self.layer[layer_number-1].display_layer()

    def lay_stone(self,stone, layer_number, x, y): 
        self.layer[layer_number-1].lay_stone(stone, x,y)
        return

    def set_layer_number(self, layer_number: int) -> None:
        self.layer_number = layer_number

    def add_stone(self, layer_num: int, stone: Stone):

        return
    
    def has_stone(self, layer_num: int, stone: Stone, x: int, y: int) -> bool: 
        return
    
    def _verify_construction_rule(self, layer_num: int, stone: Stone) -> bool:
        if layer_num == 1: 
            return True
        
        return 