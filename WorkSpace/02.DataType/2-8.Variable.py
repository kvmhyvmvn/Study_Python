# 변수_이름 = 변수에_저장할_값
# a = 1
# b = "python"
# c = [1, 2, 3]

# a = [1, 2, 3]
# [1, 2, 3] 값을 가지는 리스트 데이터(객체)가 자동으로 메모리에 생성
# print(id(a)) # 리스트가 저장된 메모리의 주소

# a = [1, 2, 3]
# b = a
# print(id(a))
# print(id(b))
# print(a is b)
# a[1] = 4
# print(a)
# print(b)

# a = [1, 2, 3]
# b = a[:]
# a[1] = 4
# print(a)
# print(b)

# copy 모듈
from copy import copy
a = [1, 2, 3]
b = copy(a) # b = a[:]와 동일
print(b is a)

a, b = ('python', 'life') # (a, b) = 'python', 'life' 와 동일
print(a)
print(b)

[a, b] = ['python', 'life']
a = b = 'python'

a = 3
b = 5
a, b = b, a
print(a)
print(b)