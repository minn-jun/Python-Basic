class Unit:
    def __init__(self):
        print("Unit 생성자")

    def spawn(self):
        print("유닛이 생성되었습니다.")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class HealUnit(Unit):
    def __init__(self):
        super().spawn()
        # super() : 자식클래스 내에서 부모클래스 메소드 호출 가능
        # 호출 시 self X

medic = HealUnit()


class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        # 다중 상속을 받을 때 super() 사용 시 먼저 상속받은 클래스에 대해서만 __init__ 호츌
        # mro()를 사용하여 우선순위 확인 가능

        # 모든 부모 클래스에 대해서 초기화가 필요한 경우 따로 명시해야 함. 
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()


# 건물
class BuildingUnit():
    def __init__(self, name, hp, location):
        pass    # 아무것도 실행하지 않고 넘어감, 오류발생 X

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# mro() 메소드 : 상속 관계 및 우선순위 확인 가능
print(FlyableUnit.mro())
# 리스트 형식으로 저장
# [<class '__main__.FlyableUnit'>, <class '__main__.Flyable'>, <class '__main__.Unit'>, <class 'object'>]
# FlyableUnit > Flyable > Unit