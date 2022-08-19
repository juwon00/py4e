def after_100(first_month,first_date,first_day):
    
    week_day = "월화수목금토일"
    day = week_day.find(first_day) + 1
    if day == 7:
        day = 0

    month = int(first_month)
    date = int(first_date)
    date = date + 99 # 조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다

    while True:
        if month == 13:
            month = month - 12
            
        if month == 2: # 조건2 - 몇년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.
            if date <= 28 and date > 0:
                break
            month = month + 1
            date = date - 28
            
        if month == 4 or month == 6 or month == 9 or month == 11:
            if date <= 30 and date > 0:
                break
            month = month + 1
            date = date - 30
            
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if date <= 31 and date > 0:
                break
            month = month + 1
            date = date - 31
            
    print(first_month+"월"+first_date+"일"+first_day+"요일 부터 100일 뒤는 "+str(month)+"월"+str(date)+"일"+week_day[day]+"요일")     


first_month,first_date,first_day = input("날짜를 입력해주세요: ").split(",")

after_100(first_month,first_date,first_day)



# def after_100(month, date, day):
#     		# 달 별로 며칠까지 있는지 리스트로 만들기
#     dates = [31,28,31,30,31,30,31,31,30,31,30,31]
#     # 요일 리스트
# 		days = ["월","화","수","목","금","토","일"]
#     after = 100
    
# 		# 파이썬 index는 0부터 시작하기 때문에 월 -1
#     index = month-1
    
#     while True:
# 				# 100일 음수가 될 때까지 날짜 차감
#         after = after - dates[index]
#         if after < 0:
#             break
#         # 12월 다음은 1월으로 돌아가기
#         index = index + 1
#         if index == 12:
#             index = 0
		
# 		# 음수가된 after에 100일 후의 월의 일수를 더해주고
# 		# 현재 일 수를 더하고 오늘을 포함하기 때문에 -1
#     date_after_100 = after + dates[index] + date -1
#     # 만약 일수가 30일, 31일을 넘어가면 100일 후의 월의 일수를 빼주고 월 +1 추가 
# 		if date_after_100 > dates[index]:
#         date_after_100 = date_after_100 - dates[index]
#         index = index + 1
#     # 요일은 7로 나눈 나머지 만큼 움직이면 됨, 오늘을 포함하기 때문에 -1
# 		day_index = days.index(day)
#     day_index2 = day_index + 100 % 7 -1
# 		# 일요일 다음은 월요일로 돌아감
#     if day_index2 > (len(days) -1):
#         day_index2 = day_index2 - (len(days) -1) -1
#     day_after_100 = days[day_index2]    
    
#     print(f"{month}월 {date}일 {day}요일부터 100일 뒤는 {index+1}월 {date_after_100}일 {day_after_100}요일")