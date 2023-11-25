# 매주 1회 보고서 제출
# 출력
# - X 주차 주간 보고 - 
# 부서 :
# 이름 : 
# 업무 요약 :

# 1주차 ~ 50주차 보고서 파일 만드는 프로그램 작성
# 조건 : 파일명은 'n주차.txt' 로 생성

for i in range(1, 50):
    with open(f"{i}주차.txt", "w", encoding="utf8") as week_file:
        week_file.write(f"- {i} 주차 주간보고 -")
        week_file.write("\n부서 : ")
        week_file.write("\n이름 : ")
        week_file.write("\n업무 요약 : ")