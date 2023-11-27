class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 4일] 방콕, 파타야 여행 (야시장 투어) 50만원")


# 실제 패키지나 모듈을 만들 때는 모듈이 잘 동작하는지 테스트를 해야 함.
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행됨.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")