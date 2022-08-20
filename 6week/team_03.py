def stock_profit(stocks,sells):
    
    stocks_li = list() # stocks를 일일이 쪼개서 stocks_li에 넣어준다
    stocks = stocks.split(",")
    for line in stocks:
        slash = line.split('/')
        for w in slash:
            stocks_li.append(w)

    earn_li = list() # 수익률을 계산해서 earn_li에 넣어준다
    for i in range(0,len(sells)): 
        earning_rate = (sells[i] / int(stocks_li[3*i+2])) * 100 - 100
        earn_li.append(f"{earning_rate:.3}")

    stock_di = dict() # stocks_li의 종목이름을 key, earn_li를 value로 갖는 딕셔너리를 만든다
    for j in range(0,len(earn_li)):
        stock_di[stocks_li[3*j]] = earn_li[j]

    last_li = list() # 마지막으로 내림차순으로 정렬하고 print한다
    for k,v in stock_di.items():
        f = (v,k)
        last_li.append(f)
        
    last_li = sorted(last_li,reverse=True)

    for v,k in last_li:
        print(f"{k}의 수익률: {v}")


stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

stock_profit(stocks,sells)