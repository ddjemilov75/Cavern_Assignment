from src.utils import draw_text
from src.constants import WIDTH, IMAGE_WIDTH, CHAR_WIDTH


class GameOverScreen:
    
    def __init__(self, final_score, final_level):
        self.final_score = final_score
        self.final_level = final_level
    
    def update(self, input_state, play_sound_callback):
        if input_state.fire_pressed:
            from src.screens.menu import MenuScreen
            return MenuScreen()
        
        return None
    
    def draw(self, screen):
        screen.fill((0, 0, 0))
        
        screen.blit("over", (0, 0))
        
        number_width = CHAR_WIDTH[0]
        score_str = str(self.final_score)
        draw_text(screen, score_str, 451, WIDTH - 2 - (number_width * len(score_str)))
        
        draw_text(screen, "LEVEL " + str(self.final_level), 451)