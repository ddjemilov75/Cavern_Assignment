from random import randint


class SoundManager:
    
    def __init__(self, sounds_module):
        self.sounds = sounds_module
    
    def play_sound(self, name, count=1):
        try:
            sound_name = name + str(randint(0, count - 1))
            sound = getattr(self.sounds, sound_name)
            sound.play()
        except Exception as e:
            print(f"Sound not found: {e}")