def wrong_guest_book(file):
    for j in file:
        i = j.split("\n")[0]
        n, m = i.split(",")
        if m[3] != "-" or m[8] != "-" or len(m) != 13 or m[:3] != "010":
            print("잘못 쓴 사람: " + str(n))
            print("잘못 쓴 번호: " + str(m) + "\n")


guest_book = open('guest_book.txt')

wrong_guest_book(guest_book)



# 코치님의 예시 코드
# def wrong_guest_book(guest_book):
#     		# text 파일 저장
#     text_save = open("guest_book.txt","w", encoding="UTF8")
#     text_save.write(guest_book)
#     text_save.close()
    
# 		# 파일 불러오기
#     file = open("guest_book.txt")
#     for line in file:
# 				# 이름과 전화번호 구분
#         name = line[:2]
#         phone_number = line[3:].strip()
# 				# 조건을 만족하면 continue 아니면 출력
#         if len(phone_number) == 13 and phone_number.find("-") != -1 and phone_number.startswith("010") == True:
#             continue
#         else:
#             print(f"잘못 쓴 사람: {name}")
#             print(f"잘못 쓴 번호: {phone_number}")
#             print()





