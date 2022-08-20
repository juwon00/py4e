info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"

info = info.split(",")



p1=[]
p2=[]
p3=[]
p4=[]
p5=[]
p6=[]
for i in info:
    if len(p1) <= 5:
        p1.append(i)
    else:
        if len(p2) <= 5:
            p2.append(i)
        else:
            if len(p3) <= 5:
                p3.append(i)
            else:
                if len(p4) <= 5:
                    p4.append(i)
                else:
                    if len(p5) <= 5:
                        p5.append(i)
                    else:
                        if len(p6) <= 5:
                            p6.append(i)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)


id_li = []
age_li = []
phone_li = []
gender_li = []
area_li = []
purchase_li = []

for i in range(0,6):
    id_li.append(info[6*i])
    age_li.append(info[6*i+1])
    if len(info[6*i+2]) == 13:
        phone_li.append(info[6*i+2])
    else:
        phone_li.append("000-0000-0000") # 조건3 - 전화번호가 없으면 000-0000-0000으로 출력할 것
    gender_li.append(info[6*i+3])
    area_li.append(info[6*i+4])
    purchase_li.append(info[6*i+5])
    
# print(id_li)
# print(age_li)
# print(phone_li)
# print(gender_li)
# print(area_li)
# print(purchase_li)

dic = dict()
for i in range(len(phone_li)):
    if phone_li[i] == '000-0000-0000': # 조건2 - 전화번호가 없으면 쿠폰을 받을 수 없음
        continue
    else:
        dic[phone_li[i]] = int(purchase_li[i])

lis = list()
for k,v in dic.items():
    newl = (v,k)
    lis.append(newl)
lis = sorted(lis,reverse=True)


print(lis)

print(lis[0])

# print("{"+f"'아이디':{id_li},'나이':{age_li},'전화번호':{phone_li},'성별':{gender_li},'지역':{area_li},'구매횟수':{purchase_li}"+"}")

# print("할인쿠폰을 받을 회원정보 아이디:")
