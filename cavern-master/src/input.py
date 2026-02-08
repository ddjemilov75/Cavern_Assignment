from dataclasses import dataclass


@dataclass
class InputState:
    left: bool
    right: bool
    up: bool
    jump_pressed: bool
    fire_pressed: bool
    fire_held: bool   
    pause_pressed: bool

class InputManager:
    
    def __init__(self):
        self._space_was_down = False
        self._p_was_down = False
    
    def get_input_state(self, keyboard) -> InputState:
        space_pressed = False
        if keyboard.space:
            if not self._space_was_down:
                space_pressed = True
                self._space_was_down = True
        else:
            self._space_was_down = False
        
        p_pressed = False
        if keyboard.p:
            if not self._p_was_down:
                p_pressed = True
                self._p_was_down = True
        else:
            self._p_was_down = False
        
        return InputState(
            left=keyboard.left,
            right=keyboard.right,
            up=keyboard.up,
            jump_pressed=keyboard.up,
            fire_pressed=space_pressed,
            fire_held=keyboard.space,
            pause_pressed=p_pressed
        )