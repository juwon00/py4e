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
