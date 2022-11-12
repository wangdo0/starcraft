from CommandCenter import CommandCenter
from Player import Player
from SCV import SCV

player = Player('BoxeR')
commandCenter = CommandCenter(player)
scvList = [
    SCV(player),
    SCV(player),
    SCV(player),
    SCV(player),
]

newScv = commandCenter.produce()
scvList.append(newScv)

for scv in scvList:
    scv.harvest()

print(player)

scvList[0].attack(scvList[1])

print(scvList[1])
