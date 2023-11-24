from random import *

comment = [i for i in range(1, 21)]
print(comment)
shuffle(comment)
a = sample(comment, 4)
print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {a[0]}")
print(f"커피 당첨자 : {a[1:]}")
print("-- 축하합니다 --")