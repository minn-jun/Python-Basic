from random import *

print(random())     # 0.0 ~ 1.0 미만 임의의 값 생성
print(random() * 10)    # 0.0 ~ 10.0 미만 임의의 값 생성

print(int(random() * 10))    # 0 ~ 10 미만 임의의 값 생성
print(int(random() * 10) + 1)   # 1 ~ 10 이하 임의의 값 생성

print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46)) # 1 ~ 45

print(randint(1, 45))   # 양 끝 포함

