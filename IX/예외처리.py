# 예외처리를 통해 프로그램의 완성도를 높일 수 있음

try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번째 숫자 입력 : ")))
    nums.append(int(input("두 번째 숫자 입력 : ")))
    nums.append(int((nums[0] / nums[1] )))
    print(f"{nums[0]} / {nums[1]} = {nums[2]}")

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError as err:    # 에러 메시지를 받을 수 있음
    print(err)

except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)

# finally
# 예외처리 구문에서 정상실행이 되든 오류가 발생하든 반드시 실행
# 위에서 처리되지 않는 오류가 발생하더라도 실행
finally:
    print("계산기를 이용해 주셔서 감사합니다.")