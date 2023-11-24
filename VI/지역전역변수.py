# 지역변수 : 함수 속에서 선언되어 해당 함수 내에서만 사용이 가능한 변수
# 전역변수 : 함수 밖에서 선언하여 전체에서 사용이 가능한 변수

gun = 10

def checkpoint(soldiers):    # 경계근무
    global gun    # 전역 공간에 있는 변수 gun을 사용하기 위해 global 사용
    gun = gun - soldiers
    print(f"[함수 내] 남은 총 : {gun}")

# 전역변수를 많이 사용하게 되면 코드 관리가 어려워짐


# 함수에 파라미터로 넘겨받아서 리턴값을 받는 형식으로 코드를 짜는게 유용
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(f"[함수 내] 남은 총 : {gun}")
    return gun

print(f"전체 총 : {gun}")
# checkpoint(2)    # 2명이 경계근무 중
gun = checkpoint_ret(gun, 2)
print(f"남은 총 : {gun}")