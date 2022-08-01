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
    if myrsp == comrsp:
        result = "비겼습니다!"
    elif myrsp == "가위" and comrsp == "바위":
        result = "컴퓨터 승리!"
    elif myrsp == "가위" and comrsp == "보":
        result = "나의 승리!"
    elif myrsp == "바위" and comrsp == "보":
        result = "컴퓨터 승리!"
    elif myrsp == "바위" and comrsp == "가위":
        result = "나의 승리!"
    elif myrsp == "보" and comrsp == "가위":
        result = "컴퓨터 승리!"
    elif myrsp == "보" and comrsp == "바위":
        result = "나의 승리!"
    else:
        result = "Error"
    return result

myrsp = input("가위 바위 보 ")
comrsp = computer()

print("나:",myrsp)
print("컴퓨터:",comrsp)
print(game_result())
