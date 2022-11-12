class Player:

    def __init__(self, name):
        self.name = name
        self.mineral = 50

    def __str__(self):
        return f"{self.name}님의 보유 미네랄 양은 {self.mineral} 입니다."