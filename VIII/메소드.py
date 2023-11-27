# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):    # 클래스 내에서 메소드 앞에는 self가 있어야 함
        print(f"{self.name} : {location}방향으로 적군 공격 [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage}피해를 입음")
        self.hp -= damage
        print(f"{self.name} : 현재 체력 {self.hp}")
        if self.hp <= 0:
            print(f"{self.name} : 파괴됨")


firebat1 = AttackUnit("파이어뱃", 50, 16)

# (객체.메소드)로 호출
firebat1.attack("5시")

# 공격을 두번 받음
firebat1.damaged(25)
firebat1.damaged(25)
