# 딕셔너리 {key : value}

cabinet = {3 : "이순신", 100 : "홍길동"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])        # key가 없을 경유 error 발생 후 종료
# print(cabinet.get(5))    # key가 없을 경우 None 반환 후 continue
print(cabinet.get(5, "사용 가능"))    # None 대신 다른 내용 반환

# 딕셔너리 안에 값이 있는지 확인
print(3 in cabinet)   # True
print(5 in cabinet)   # False

new_dic = {"A-1" : "류현진", "C-9" : "김광현"}
print(new_dic["A-1"])
print(new_dic["C-9"])

# 새로운 값 추가
print(new_dic)
new_dic["A-1"] = "박병호"
new_dic["H-15"] = "양현종"
print(new_dic)

# 값 제거
del new_dic["A-1"]
print(new_dic)

# key들만 출력
print(new_dic.keys())

# value들만 출력
print(new_dic.values())

# key, value 쌍으로 출력
print(new_dic.items())

# 모든 값 제거
new_dic.clear()
print(new_dic)