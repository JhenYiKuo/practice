#!usr/bin/python3.10.4
import random

def playgame():
    min = 1
    max = 100
    count = 0
    target = random.randint(min, max)
    print(target)
    print('=====猜數字遊戲開始=====')

    while True:
        keyin = int(input(f'猜數字遊戲範圍{min}~{max}:'))
        count += 1
        if (keyin == target):
            print(f'猜對了，答案是:{target}')
            print(f'您總共猜了{count}次')
            break
        elif keyin > target:
            print('再小一點')
            max = keyin -1
        elif keyin < target:
            print('再大一點')
            min = keyin +1
        print(f'您已經猜了{count}次')

while(True):
    playgame()
    play_again = (input('還要再來一把嗎？(y,n)'))
    if not (play_again == 'y'):
        break
print('遊戲結束')