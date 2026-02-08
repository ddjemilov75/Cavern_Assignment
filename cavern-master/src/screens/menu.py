from src.game import Game


class MenuScreen:
    
    def __init__(self):
        self.game = Game()
    
    def update(self, input_state, play_sound_callback):
        if input_state.fire_pressed:
            from src.screens.play import PlayScreen
            return PlayScreen()
        
        from src.input import InputState
        empty_input = InputState(False, False, False, False, False, False, False)
        self.game.update(empty_input, play_sound_callback)
        
        return None
    
    def draw(self, screen):
        self.game.draw(screen)
        
        screen.blit("title", (0, 0))
        
        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim_frame), (130, 280))