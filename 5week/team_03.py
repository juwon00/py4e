def guess_numbers():
    import random

    num_list = list()
    while True: # 조건1 - 숫자는 0 ~ 100까지 숫자를 3개 만듭니다(중복 불가).
        number = random.randint(0,100)
        
        if number in num_list:
            continue
        
        num_list.append(number)
        
        if len(num_list) == 3:
            break

    num_list.sort()
    print(num_list)

    i = 0
    count = 0
    score_list = list()
    while True:
        print(count+1,"차 시도")
        input_num = int(input("숫자를 예측해보세요:"))
        
        if input_num in score_list:
            print("이미 예측에 사용한 숫자입니다.")
            print()
            continue

        if input_num in num_list: #조건3 - 정답을 맞추면, 맞춘 정답이 최솟값인지, 중간값인지, 최댓값인지 알려줍니다.
            
            if input_num == num_list[0]:
                print("숫자를 맞추셨습니다!",input_num,"는 최솟값입니다.")
            elif input_num == num_list[1]:
                print("숫자를 맞추셨습니다!",input_num,"는 중간값입니다.")
            elif input_num == num_list[2]:
                print("숫자를 맞추셨습니다!",input_num,"는 최댓값입니다.")
                
            i = i + 1
            count = count + 1
            score_list.append(input_num)
            
        else:   
            print(input_num,"는 없습니다.")
            count = count + 1
            score_list.append(input_num)
            
            if count%5 == 0: # 조건2 - 5회, 10회까지 정답을 못맞추면 최솟값, 최대값에 대한 힌트를 줍니다.    
                if input_num < num_list[0]:
                    print("최솟값은",input_num,"보다 큽니다.")
                elif input_num > num_list[0] and input_num < num_list[1]:
                    print("최솟값은",input_num,"보다 작습니다.")
                elif input_num > num_list[1] and input_num < num_list[2]:
                    print("최댓값은",input_num,"보다 큽니다.")
                elif input_num > num_list[2]:
                    print("최댓값은",input_num,"보다 작습니다.")
        print()
        
        if i == 3:
            print("게임종료")
            print(count,"번 시도만에 예측 성공!")
            break

        
guess_numbers()