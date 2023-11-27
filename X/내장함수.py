# 내장함수 : 따로 import 없이 바로 사용 가능한 함수
'''
list of python builtins
https://docs.python.org/ko/3.11/library/functions.html
파이썬 내장함수 확인 가능
'''


# input() : 사용자 입력을 받는 함수
language = input("어떤 언어를 좋아하세요? : ")
print(f"{language}은 아주 좋은 언어입니다!")

# dir() : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random    # 외장 함수
print(dir())
import pickle
print(dir())

print(dir(random))

lst = [1, 2, 3]
print(dir(lst))

name = "Jim"
print(dir(name))