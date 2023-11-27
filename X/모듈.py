# module : 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일 (.py)
# 모듈이 모듈을 쓰려는 파일과 같은 경로에 있거나 파이썬 라이브러리들이 모인 폴더에 있을 경우 사용 가능

'''
import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_solider(5)
'''

'''
# 모듈의 이름이 길 경우 as로 별칭을 붙여서 사용 가능
import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_solider(5)
'''

'''
# 모듈의 모든 내용을 바로 사용 가능
from theater_module import *
# from random import *
price(3)
price_morning(4)
price_solider(5)
'''

'''
# 필요한 함수만 import
from theater_module import price, price_morning
price(5)
price_morning(6)
'''

'''
# 사용할 함수를 as로 별칭을 붙여서 사용 가능
from theater_module import price_solider as price
price(5)    # price_soldier
'''