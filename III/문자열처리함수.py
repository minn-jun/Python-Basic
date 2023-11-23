python = "Python is Amazing"
print(python.lower())   # 전부 소문자로
print(python.upper())   # 전부 대문자로
print(python[0].isupper())  # 인덱스 값이 대문자인지? (Bool)
print(len(python))      # 문자열 길이 반환
print(python.replace("Python", "Java"))  # 변경

index = python.index("n")
print(index)
index = python.index("n", index + 1)  # 다음번 n 찾기
print(index)

print(python.find("n"))
print(python.find("Java"))      # 찾는 문자열이 없는 경우 -1 반환 후 continue
# print(python.index("Java"))     # 찾는 문자열이 없는 경우 error 발생 후 종료
print("hello world")

print(python.count("n"))    # 개수 찾기