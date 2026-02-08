from src.game import Game
from src.entities.player import Player
from src.utils import draw_text
from src.constants import WIDTH, IMAGE_WIDTH, CHAR_WIDTH


class PlayScreen:    
    def __init__(self):
        self.game = Game(Player())
        self.paused = False
    
    def update(self, input_state, play_sound_callback):

        if input_state.pause_pressed:
            self.paused = not self.paused
            return None
        
        if self.paused:
            return None
        
        if self.game.player.lives < 0:
            play_sound_callback("over")
            from src.screens.game_over import GameOverScreen
            return GameOverScreen(self.game.player.score, self.game.level + 1)
        
        self.game.update(input_state, play_sound_callback)
        
        return None
    
    def draw(self, screen):
        self.game.draw(screen)
        
        self._draw_status(screen)
        
        if self.paused:
            self._draw_pause_overlay(screen)
    
    def _draw_status(self, screen):
        number_width = CHAR_WIDTH[0]
        score_str = str(self.game.player.score)
        draw_text(screen, score_str, 451, WIDTH - 2 - (number_width * len(score_str)))
        
        draw_text(screen, "LEVEL " + str(self.game.level + 1), 451)
        
        lives_health = ["life"] * min(2, self.game.player.lives)
        if self.game.player.lives > 2:
            lives_health.append("plus")
        if self.game.player.lives >= 0:
            lives_health += ["health"] * self.game.player.health
        
        x = 0
        for image in lives_health:
            screen.blit(image, (x, 450))
            x += IMAGE_WIDTH[image]
    
    def _draw_pause_overlay(self, screen):
        draw_text(screen, "PAUSED", 200)
        draw_text(screen, "PRESS P TO RESUME", 250)