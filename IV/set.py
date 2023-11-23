# 집합 set > 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {'a', 'b', 'c'}
python = set({'a', 'd'})

# 교집합 (java, python 둘다 포함)
print(java & python)
print(java.intersection(python))

# 합집합 (java 또는 python 포함)
print(java | python)
print(java.union(python))

# 차집합 (java만 포함)
print(java - python)
print(java.difference(python))

# 집합에 데이터 추가
python.add('c')
print(python)

# 집합에 데이터 삭제
java.remove('c')
print(java)