han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    
    # if line == ' ':
    #     continue
    # 이 두줄 또한 가디언
    
    wds = line.split()
    # Guardian  
    # or 앞에 나오는 식을 먼저 확인하고 뒤로 넘어가므로 가디언 식을 앞에 위치시킨다.
    if len(wds) < 3 or wds[0] != 'From': # 1이 아닌 3인 이유는 아래 wds[2]를 보호하기 위해
        continue
    print(wds[2]) 