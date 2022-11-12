class Firebat:

    def __init__(self, player):
        self.player = player
        self.hp = 50

    def __str__(self):
        return f"[{self.player.name}] Firebat [{self.hp}/50]"

    def attack(self, target):
        target.hp -= 16