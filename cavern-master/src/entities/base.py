from pgzero.actor import Actor
from src.constants import ANCHOR_CENTRE, ANCHOR_CENTRE_BOTTOM, HEIGHT, GRID_BLOCK_SIZE
from src.utils import block, sign


class CollideActor(Actor):    
    def __init__(self, pos, anchor=ANCHOR_CENTRE):
        super().__init__("blank", pos, anchor)
    
    def move(self, dx, dy, speed, grid):
        new_x, new_y = int(self.x), int(self.y)
        
        for i in range(speed):
            new_x, new_y = new_x + dx, new_y + dy
            
            if new_x < 70 or new_x > 730:
                return True
            
            if ((dy > 0 and new_y % GRID_BLOCK_SIZE == 0 or
                 dx > 0 and new_x % GRID_BLOCK_SIZE == 0 or
                 dx < 0 and new_x % GRID_BLOCK_SIZE == GRID_BLOCK_SIZE - 1)
                and block(new_x, new_y, grid)):
                return True
            
            self.pos = new_x, new_y
        
        return False


class GravityActor(CollideActor):
    
    MAX_FALL_SPEED = 10
    
    def __init__(self, pos):
        super().__init__(pos, ANCHOR_CENTRE_BOTTOM)
        self.vel_y = 0
        self.landed = False
    
    def update_gravity(self, grid, detect=True):
        self.vel_y = min(self.vel_y + 1, GravityActor.MAX_FALL_SPEED)
        
        if detect:
            if self.move(0, sign(self.vel_y), abs(self.vel_y), grid):
                self.vel_y = 0
                self.landed = True
            
            if self.top >= HEIGHT:
                self.y = 1
        else:
            self.y += self.vel_y