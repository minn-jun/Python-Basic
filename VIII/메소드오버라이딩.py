# 메소드 오버라이딩
# 부모클래스의 메소드를 자식 클래스에서 재정의

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    # move 매소드 정의
    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location}방향으로 이동. [속도 {self.speed}]")


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location}방향으로 적군 공격 [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage}피해를 입음")
        self.hp -= damage
        print(f"{self.name} : 현재 체력 {self.hp}")
        if self.hp <= 0:
            print(f"{self.name} : 파괴됨")


# 비행 기능
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location}방향으로 비행. [속도 {self.flying_speed}]")


# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)    # 지상 속도 0
        Flyable.__init__(self, flying_speed)

    # move 메소드 재정의
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")

# 공중유닛으로 move를 호출하면 재정의된 move 호출
battlecruiser.move("9시")