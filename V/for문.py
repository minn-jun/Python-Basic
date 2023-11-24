# for 반복문
for waiting_no in range(1, 6):
    print(f"대기번호 : {waiting_no}")

cafe = ['a', 'b', 'c']
for customer in cafe:
    print(f"{customer}, 음료가 준비되었습니다.")


# 한 줄 for
# 출석번호가 1, 2, 3, 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "Groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students)