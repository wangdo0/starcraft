from Firebat import Firebat


class Barracks:

    def __init__(self, player):
        self.player = player

    def produce(self):
        self.player.mineral -= 50
        self.player.gas -= 25
        f = open("log.csv", "a")
        f.write(f"{self.player.name}, 파이어뱃, 생성, 1\n")
        f.close()
        return Firebat(self.player)