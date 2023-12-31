# 부동산 프로그램 작성

# 출력
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# 코드
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")


building = []
b1 = House("강남", "아파트", "매매", "10억", "2010년")
b2 = House("마포", "오피스텔", "전세", "5억", "2007년")
b3 = House("송파", "빌라", "월세", "500/50", "2000년")

building.append(b1)
building.append(b2)
building.append(b3)

print(f"총 {len(building)}대의 매물이 있습니다.")
for b in building:
    b.show_detail()