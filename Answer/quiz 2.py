# 랜덤으로 날짜 선택
# 28일 이내
# 1~3일 제외

from random import *

date = randint(4, 28)
print(f"오프라인 스터디 모임 날짜는 매월 {date}일로 선정되었습니다.")