# 상속하는 클래스 : 부모 클래스
# 상속받은 클래스 : 자식 클래스

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


# 공격 유닛
class AttackUnit(Unit):    # ()안의 클래스를 상속 받음
    def __init__(self, name, hp, damage):
        # 상속을 받았기 때문에 Unit에 있는 self.name, self.hp 사용 가능
        Unit.__init__(self, name, hp)
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
# 다중 상속 : 부모 클래스가 2 이상
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "5시")
valkyrie.attack("5시")