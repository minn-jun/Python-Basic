# 문자열 String
# 파이썬에서는 "", '' 크게 상관 X

sentence = 'I am human.'
print(sentence)
sentence2 = "I love Python."
print(sentence2)

sentence3 = """
I am human.
I love Python.
"""
print(sentence3)


# 슬라이싱
person_id = "990530-1234567"
print("성별 : " + person_id[7])
print("연 : " + person_id[:2])
print("월 : " + person_id[2:4])
print("일 : " + person_id[4:6])

print("생년월일 : " + person_id[:6])
print("뒤 7자리 : " + person_id[7:])
print("뒤 7자리 : " + person_id[-7:])   # 뒤에서부터 계산

