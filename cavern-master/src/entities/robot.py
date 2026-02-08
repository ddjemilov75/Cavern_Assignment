from random import randint, choice, random
from src.entities.base import GravityActor
from src.utils import sign


class Robot(GravityActor):
    
    TYPE_NORMAL = 0
    TYPE_AGGRESSIVE = 1
    
    def __init__(self, pos, robot_type):
        super().__init__(pos)
        self.type = robot_type
        self.speed = randint(1, 3)
        self.direction_x = 1
        self.alive = True
        self.change_dir_timer = 0
        self.fire_timer = 100
    
    def update(self, grid, player, orbs, bolts, game_timer, fire_probability, play_sound_callback):
        self.update_gravity(grid)
        
        self.change_dir_timer -= 1
        self.fire_timer += 1
        
        if self.move(self.direction_x, 0, self.speed, grid):
            self.change_dir_timer = 0
        
        if self.change_dir_timer <= 0:
            directions = [-1, 1]
            if player:
                directions.append(sign(player.x - self.x))
            self.direction_x = choice(directions)
            self.change_dir_timer = randint(100, 250)
        
        if self.type == Robot.TYPE_AGGRESSIVE and self.fire_timer >= 24:
            for orb in orbs:
                if orb.y >= self.top and orb.y < self.bottom and abs(orb.x - self.x) < 200:
                    self.direction_x = sign(orb.x - self.x)
                    self.fire_timer = 0
                    break
        
        if self.fire_timer >= 12:
            fire_prob = fire_probability
            if player and self.top < player.bottom and self.bottom > player.top:
                fire_prob *= 10
            
            if random() < fire_prob:
                self.fire_timer = 0
                play_sound_callback("laser", 4)
        elif self.fire_timer == 8:
            from src.entities.bolt import Bolt
            bolt = Bolt((self.x + self.direction_x * 20, self.y - 38), self.direction_x)
            bolts.append(bolt)
        
        for orb in orbs:
            if orb.trapped_enemy_type is None and self.collidepoint(orb.center):
                self.alive = False
                orb.floating = True
                orb.trapped_enemy_type = self.type
                play_sound_callback("trap", 4)
                break
        
        direction_idx = "1" if self.direction_x > 0 else "0"
        image = "robot" + str(self.type) + direction_idx
        if self.fire_timer < 12:
            image += str(5 + (self.fire_timer // 4))
        else:
            image += str(1 + ((game_timer // 4) % 4))
        self.image = image