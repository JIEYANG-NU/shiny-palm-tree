"""
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
"""
import random
gabberone = random.randint(2, 12)
money = 100000
for j in range(1000):
    while(j==1):
        if gabberone == 7 or gabberone == 11:
            money += 100
            print('玩家胜利！')
            break
        elif gabberone == 2 or gabberone == 12:
             money -= 100
             print('庄家胜利！')
             break
    for i in range(1000):
        if money < 0:
            break
        else:
            gabber = random.randint(2, 12)
            if gabber == 7:
                money -= 100
                print('庄家胜利！')
            elif gabber == gabberone:
                money += 100
                print('玩家胜利！')
            else:
                continue
    break
print('您已破产！')

