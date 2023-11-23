# 문자열 format

print("a" + "b")
print("a", "b")


# 방법 1
print("I am %d years old." % 20)       # 숫자
print("I love %s." % "apple")          # 문자열
print("Apple은 %c로 시작해요." % "A")   # 문자
# 전부 %s로 대체 가능
print("I love %s and %s." % ("Red", "Blue"))


# 방법 2
print("ㅑam {} years old.".format(20))
print("I love {0} and {1}.".format("Red", "Blue"))
print("I love {1} and {0}.".format("Red", "Blue"))


# 방법 3
print("I am {age} years old, I love {color}.".format(age=20, color="Red"))


# 방법 4 > fstring
age = 20
color = "Red"
print(f"I'm {age} years old, I love {color}.")