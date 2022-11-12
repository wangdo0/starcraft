class SCV:

    def __init__(self, player):
        self.player = player
        self.hp = 60

    def __str__(self):
        return f"[{self.player.name}] SCV [{self.hp}/60]"

    def harvest(self):
        self.player.mineral += 8

    def attack(self, target):
        target.hp -= 8