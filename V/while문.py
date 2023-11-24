# while 반복문
customer = "토르"
index = 5
while index >= 1:
    print(f"{customer}, 음료가 준비되었습니다.")
    print(f'{index}번 남았어요.')
    index -= 1
    if index == 0:
        print("음료가 폐기처분 되었습니다.")

# 무한루프 >> Terminal에서 Ctrl + C 입력 시 종료
# customer = "아이언맨"
# index = 1
# while True:
#     print(f"{customer}, 음료가 준비되었습니다.")
#     print(f"호출 {index}회")
#     index += 1

customer = "토르"
person = "Unknown"
while person != customer:
    print(f"{customer}, 음료가 준비되었습니다.")
    person = input("이름이 어떻게 되세요? : ")