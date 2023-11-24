# 표준 체중 구하는 프로그램 작성
# 남성 : 키(m) ^ 2 * 22
# 여성 : 키(m) ^ 2 * 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# 출력
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남자":
        weight = ((height / 100) ** 2) * 22

    elif gender == "여자":
        weight = ((height / 100) ** 2) * 21

    print(f"키 {height}cm {gender}의 표준 체중은 {round(weight, 2)}kg 입니다.")

std_weight(175, "남자")