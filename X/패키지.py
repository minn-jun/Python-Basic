# package : module의 집합

'''
# import 구문에서는 패키지, 모듈만 직접 import 가능
import travel.thailand
# import travel.thailand.ThailandPackage()    # 클래스, 함수 직접 import 불가
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
'''

'''
# from - import 구문에서는 패키지, 모듈, 클래스, 함수 등 직접 import 가능
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()
'''

'''
from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()
'''


from travel import *
# * 을 사용하는 경우 개발자가 문법 상에서 공개 범위를 설정해야 함.
# 패키지 안에 포함된 것들 중에서 import 되기를 원하는 것만 공개를 하고, 원하지 않는 것은 비공개로 설정 가능
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to = thailand.ThailandPackage()
trip_to.detail()
