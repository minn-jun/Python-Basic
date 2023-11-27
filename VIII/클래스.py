# # 마린
# name = "Marine"
# hp = 40
# damage = 5
# print(f"{name}유닛이 생성되었습니다.")
# print(f"체력 : {hp}, 공격력 : {damage}\n")


# # 탱크
# t_name = "Tank"
# t_hp = 150
# t_damage = 35
# print(f"{t_name}유닛이 생성되었습니다.")
# print(f"체력 : {t_hp}, 공격력 : {t_damage}\n")


# # 공격 함수
# def attack(name, location, damage):
#     print(f"{name} : {location}방향으로 적군 공격. [공격력 {damage}]")

# attack(name, "1시", damage)
# attack(t_name, "1시", t_damage)


# Class를 만들어 유닛 생성
class Unit:
    def __init__(self, name, hp, damage):
    # __init__ : 생성자, 객체 초기화, 객체가 만들어질 때 자동으로 호출

        # 멤버변수 : 클래스 내에서 정의된 변수
        self.name = name
        self.hp = hp
        self.damage = damage

        print(f"{self.name}유닛이 생성되었습니다.")
        print(f"체력 : {self.hp}, 공격력 : {self.damage}\n")

# marine1, marine2, tank1 ... >> object 객체
# marine1, marine2, tank1 ... 객체는 Unit class의 instance 인스턴스

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)
# __init__ 에 정의된 수 만큼 정보를 넘겨주어야 함.
# tank = Unit("Tank", 150) >> Error

wraith1 = Unit("레이스", 80, 5)
# 외부에서 (객체.멤버변수)로 접근가능
print(f"유닛이름 : {wraith1.name}, 공격력 : {wraith1.damage}\n")

wraith2 = Unit("뺏긴 레이스", 80, 5)
# 외부에서 새로운 변수 할당. 해당 객체에서만 사용 가능
wraith2.clocking = True
if wraith2.clocking == True:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")