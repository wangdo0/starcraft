from SCV import SCV


class CommandCenter:

    def __init__(self, player):
        self.player = player

    def produce(self):
        self.player.mineral -= 50
        f = open("log.csv", "a")
        f.write(f"{self.player.name}, 건설로봇, 생성, 1\n")
        f.close()
        return SCV(self.player)