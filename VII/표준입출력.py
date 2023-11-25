print("Python", "Java", "Javascript", sep=", ", end="? ")
print("무엇이 더 재미있을까요?")


import sys
print("Python", "Java", file=sys.stdout)    # 표준출력
print("Python", "Java", file=sys.stderr)    # 표준에러
# stderr을 사용해서 에러처리 가능


# 시험성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # ljust(n) / rjust(n) : n만큼의 공간 만들고 좌(우)로 정렬


# 은행 대기순번표
# 001, 002, 003, 004, ....
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    # zfill(n) : n의 공간 확보 후 값을 넣고 빈공간은 0으로 채움 


# 표준 입력
answer = input("입력 : ")    # input은 항상 문자열로 저장됨.
print(type(answer))
print(f"입력값은 {answer}입니다.")