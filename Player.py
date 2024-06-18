import pyglet
from pyglet import shapes
class Player:
    def __init__(self) -> None:
        self.score = 0
    
    def add_to_score(self) -> int:
        self.score = self.score + 1
        return self.score
    
    def return_score(self) -> int:
        return self.score
    
    def reset2zero(self) -> None:
        self.score = 0
    
    
    



