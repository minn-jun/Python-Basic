# 튜플 > 내용 변경이나 수정 불가, 속도가 리스트보다 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")    # 사용불가

# name = "손흥민"
# age = 20
# hobby = "축구"
# print(name, age, hobby)

(name, age, hobby) = ("손흥민", 20, "축구")
print(name, age, hobby)