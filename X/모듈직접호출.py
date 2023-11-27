import inspect
import random
from travel import *

# inspect.getfile() >> 파일의 위치 정보를 받을 수 있음.
print(inspect.getfile(random))
print(inspect.getfile(thailand))

# 만든 패키지를 Python\Lib 경로에 넣으면 다른 프로젝트에서도 사용 가능