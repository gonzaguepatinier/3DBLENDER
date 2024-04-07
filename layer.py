from dataclasses import dataclass
from typing import List, Union
from enum import Enum
from stone import Stone, StoneQuality
import bpy

@dataclass
class Layer:
    grid: List[List[Union[Stone,None]]]
    layer_number: int
    grid_size: int

    def __init__(self, layer_number: int, grid_size: int):
        self.layer_number = layer_number
        self.grid_size = grid_size
        self.grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]

    def display_layer(self) -> None:
        print(f'Layer {self.layer_number} - {self.grid_size}x{self.grid_size}', self.layer_number)
        # for row in self.grid:
        #     print(row)
        # TODO: To refactor code below

        for row in self.grid:
            for item in row:
                if item is None:
                    print('-', end='')
                else:
                    if item.quality == StoneQuality.HIGH:
                        print('H', end='')
                    if item.quality == StoneQuality.LOW:
                        print('L', end='')
                  
            print("\n")
    def display3d_layer(self) -> None:
        print(f'Layer {self.layer_number} - {self.grid_size}x{self.grid_size}', self.layer_number)
        # for row in self.grid:
        #     print(row)
        x = float(self.layer_number) - 1 
        # z = 1 + ((self.layer_number - 1 )*2) # Correct Zyy
        z = (float(self.layer_number) * 2)  - 1.0 
        for row in self.grid:
            # x = x + float(self.layer_number)*2 - 1.0
            x = x + 2.0
            # y = (self.layer_number * 2) -1
            # y = self.layer_number 
            y = float(self.layer_number) + 1.0
            for item in row:
                y = y + 2.0
                if item is None:
                    print('-', end='')
                else:
                    print(f'x: {x} y: {y} z: {z}')
                    if item.quality == StoneQuality.HIGH:
                        bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
                        print('H', end='')
                    if item.quality == StoneQuality.LOW:
                        bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
                        print('L', end='')
                  
            print("\n")

    def lay_stone(self,stone,x,y) -> None:
        if stone.layed == True:
            return False
        if self.grid[y-1][x-1] is not None:
            return False
        stone.lay_stone(self.layer_number, x, y)   
        self.grid[y-1][x-1] = stone