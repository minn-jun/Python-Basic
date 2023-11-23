print("hello world")


# 문자열 index, find >> 찾는 문자열의 시작 인덱스 반환
python = "Hello Python"
# print(python.index("Java"))     # 찾는 문자열이 없으면 error 발생 후 종료
# print(python.find("Java"))        # 찾는 문자열이 없으면 -1 반환 후 continue
print(python.index("Python"))
print(python.find("Python"))