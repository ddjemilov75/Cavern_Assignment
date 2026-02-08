from pgzero.actor import Actor


class Pop(Actor):
    
    def __init__(self, pos, pop_type):
        super().__init__("blank", pos)
        self.type = pop_type
        self.timer = -1
    
    def update(self):
        self.timer += 1
        self.image = "pop" + str(self.type) + str(self.timer // 2)