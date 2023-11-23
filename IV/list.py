# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ['a', 'b', 'c']
print(subway)

# b가 몇번째에 있는지?
print(subway.index('b'))

# d가 다음 정류장에서 다음칸에 탑승
subway.append('d')
print(subway)

# e가 a, b 사이에 탑승
subway.insert(1, 'e')
print(subway)

# 지하철에 있는 사람을 뒤에서 한 명씩 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append('a')
print(subway)
print(subway.count('a'))

# 정렬
num_lst = [5, 1, 2, 4, 3]
num_lst.sort()
print(num_lst)

# 순서 뒤집기
num_lst.reverse()
print(num_lst)

# 모두 지우기
num_lst.clear()
print(num_lst)

# 다양한 자료형 함께 사용
a = [5, 2, 4, 3, 1]
b = ["hello", 20, False]
print(b)

# 리스트 확장
a.extend(b)
print(a)