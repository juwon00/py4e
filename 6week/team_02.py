def sales_management(member_names,member_records):
    member_average = list() # 월별 실적 평균 리스트 만들기
    for i in member_records:
        listsum = sum(i)/12
        member_average.append(listsum)

    member_di = dict() # names를 key로 records를 value로 딕셔너리 만들기
    for i in range(0,len(member_names)):
        member_di[member_names[i]] = member_average[i]

    member = list() # 내림차순으로 리스트 정렬하기
    for k,v in member_di.items():
        tup = (v,k)
        member.append(tup)
    member = sorted(member,reverse=True)

    for v,k in member[:2]: # 조건 1 - 예비 보너스 대상자는 평균 실적 1등 2등 입니다.
        if v >= 5: # 조건 3 - 보너스 대상자의 평균 실적이 5보다 크지 않으면 보너스 대상자에서 제외 됩니다.
            print("보너스 대상자:",k)
    print()
    for v,k in member[4:]: # 조건 2 - 예비 면담 대상자는 평균 실적 5등 6등 입니다.
        if v <= 3: # 조건 4 - 면담 대상자의 평균 실적이 3보다 크면 면담 대상자에서 제외 됩니다.
            print("면답 대상자:",k)
            
            
            
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
            [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
            [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

sales_management(member_names,member_records)
