# continue, break
absent = [2, 5]     # 결석
no_book = [7]       # 책이 없음

for student in range(1, 11):
    
    if student in absent:
        continue    # 아래문장을 실행하지 않고 다음 반복으로 넘어감

    elif student in no_book:
        print(f"수업 끝. {student}는 교무실로.")
        break       # break가 속한 해당 반복문 종료

    print(f"{student}, 책을 읽어봐.")