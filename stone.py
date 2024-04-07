from dataclasses import dataclass
from typing import Union
from enum import Enum


class StoneQuality(Enum):
    HIGH = "H"
    LOW = "L"

class StoneLocation(Enum):
    QUARRY = "Q"
    TRANSPORT = "T"
    PYRAMID = "P"

@dataclass 
class Stone:
    x: int = None
    y: int = None
    quality: StoneQuality = None
    location: StoneLocation = None
    layed: bool = False
    number: int = None
    layer: int = None

 
    
    def transport_stone(self, new_location: StoneLocation) -> None:
        self.location = new_location
        return
    
    def lay_stone(self, layer_number: int, x: int, y: int) -> bool:
        if self.layed == True:
            return False
        self.layed = True
        self.x = x
        self.y = y
        self.layer = layer_number
        return True


def quarry_stone(quality: StoneQuality, number: int) -> Stone:
        stone = Stone()
        stone.quality = quality
        stone.number = number
        return (stone)