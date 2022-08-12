import random

def computer_turn():
    global bs_num
    computer_turn_number = random.randint(1,3)

    if computer_turn_number == 1:
        bs_num.append(bs_num[-1] + 1)
        print("컴퓨터:",bs_num[-1])
    elif computer_turn_number == 2:
        bs_num.append(bs_num[-1] + 1)
        print("컴퓨터:",bs_num[-1])
        bs_num.append(bs_num[-1] + 1)
        print("컴퓨터:",bs_num[-1])
    elif computer_turn_number == 3:
        bs_num.append(bs_num[-1] + 1)
        print("컴퓨터:",bs_num[-1])
        bs_num.append(bs_num[-1] + 1)
        print("컴퓨터:",bs_num[-1])
        bs_num.append(bs_num[-1] + 1)
        print("컴퓨터:",bs_num[-1])



def bs31():
    global bs_num
    print("베스킨라빈스 써리원 게임")
    print("-------------------------")
    
    while True:
        my = input("My turn - 숫자를 입력하세요:").split()
        my = list(map(int, my))
        bs_num = bs_num + my
        print("현재 숫자:",bs_num[-1])
        
        computer_turn()
        print("현재 숫자:",bs_num[-1])
        
        if len(bs_num) >= 31:
            print("게임 종료")
            break
        
        

bs_num = list()
bs31()