from src.input import InputManager
from src.screens.menu import MenuScreen


class App:
    
    def __init__(self, play_sound_callback):
        self.current_screen = MenuScreen()
        self.input_manager = InputManager()
        self.play_sound_callback = play_sound_callback
    
    def change_screen(self, new_screen):
        if new_screen is not None:
            self.current_screen = new_screen
    
    def update(self, keyboard):
        input_state = self.input_manager.get_input_state(keyboard)
        
        next_screen = self.current_screen.update(input_state, self.play_sound_callback)
        self.change_screen(next_screen)
    
    def draw(self, screen):
        self.current_screen.draw(screen)