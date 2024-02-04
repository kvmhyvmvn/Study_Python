# 리스트명 = [요소1, 요소2, 요소3, ...]
# odd = [1, 3, 5, 7, 9]
# print(type(odd))

# a = [1, 2, 3, ['a', 'b', 'c']]
# print(a[0] + a[1])
# print(a[3])
# print(a[3][2])

# a = [1, 2, 3, 4, 5]
# print(a[::2]) # 문자열이랑 방법 동일

# a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# print(a[2:5])

# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)

# a = [1, 2, 3]
# print(len(a))
# print(str(a[2])+"hi")
# a[2] = 4
# print(a)

# a = [1, 2, 3, 4, 5]
# del a[1] # [n]번째 요솟값 삭제
# print(a)

# a = [1, 2, 3]
# a.append(4)
# a.append([5, 6])
# print(a)

# a = [1, 4, 3, 2]
# a.sort() # 정렬(오름차순)
# print(a)
# a.reverse()
# print(a) # 내림차순

# a = [1, 2, 3]
# print(a.index(1)) # 리스트에 값이 있으면 인덱스 값 출력
# a.insert(0, 4) # 0번째 인덱스에 4를 삽입
# print(a)
# a.remove(3)
# print(a)

# a = [1, 2, 3]
# print(a.pop()) # 맨 끝 요소 pop
# print(a)
# a.pop(1) # n번째 요소 pop
# print(a)

# a = [1, 2, 3, 1]
# print(a.count(1)) # 요소 갯수

a = [1, 2, 3]
a.extend([4, 5])
print(a)