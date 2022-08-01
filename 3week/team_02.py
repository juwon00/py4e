import random

def computer():
    a = random.randint(0,2)
    if a == 0:
        rsp = "가위"
    elif a == 1:
        rsp = "바위"
    else:
        rsp = "보"
    return rsp

def game_result():
    global my_win, my_lose, compu_win, compu_lose, draw

    if myrsp == comrsp:
        result = "비겼습니다!"
        draw = draw + 1

    elif myrsp == "가위" and comrsp == "바위":
        result = "컴퓨터 승리!"
        compu_win = compu_win + 1
        my_lose = my_lose + 1

    elif myrsp == "가위" and comrsp == "보":
        result = "나의 승리!"
        my_win = my_win + 1
        compu_lose = compu_lose + 1

    elif myrsp == "바위" and comrsp == "보":
        result = "컴퓨터 승리!"
        compu_win = compu_win + 1
        my_lose = my_lose + 1

    elif myrsp == "바위" and comrsp == "가위":
        result = "나의 승리!"
        my_win = my_win + 1
        compu_lose = compu_lose + 1

    elif myrsp == "보" and comrsp == "가위":
        result = "컴퓨터 승리!"
        compu_win = compu_win + 1
        my_lose = my_lose + 1

    elif myrsp == "보" and comrsp == "바위":
        result = "나의 승리!"
        my_win = my_win + 1
        compu_lose = compu_lose + 1

    else:
        result = "Error"
    return result


games = int(input("몇 판을 진행하시겠습니까? : "))

my_win = 0
my_lose = 0
compu_win = 0
compu_lose = 0
draw = 0

i = 1
while games > 0:

    myrsp = input("가위 바위 보 : ")
    # ("0" or "1" or "2" or "가위" or "바위" or "보")
    if myrsp == "0":
        myrsp = "가위"
    elif myrsp == "가위":
        myrsp = "가위"
    elif myrsp == "1":
        myrsp = "바위"
    elif myrsp == "바위":
        myrsp = "바위"
    elif myrsp == "2":
        myrsp = "보"
    elif myrsp == "보":
        myrsp = "보"
    else:
        print("다시 입력해주세요")
        continue

    comrsp = computer()
    print("나:",myrsp)
    print("컴퓨터:",comrsp)
    print(i,"번째 판",game_result(),"\n")
    i = i + 1
    games = games - 1

print("나의 전적:",str(my_win)+"승",str(draw)+"무",str(my_lose)+"패")
print("컴퓨터의 전적:",str(compu_win)+"승",str(draw)+"무",str(compu_lose)+"패")
