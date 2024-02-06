# 리스트는 [], 튜플은 ()

# t1 = ()
# print(type(t1))
# t2 = (1,) # 1개의 요소만을 가질 때는 뒤에 쉼표
# print(t2[0])
# t3 = (1, 2, 3)
# t4 = 1, 2, 3 # 소괄호 생략 가능
# print(t4)
# t5 = ('a', 'b', ('ab', 'cd'))

# t1 = (1, 2, 'a', 'b')
# del t1[0] # 튜플은 변경 불가능(TypeError: 'tuple' object doesn't support item deletion)

# t1 = (1, 2, 'a', 'b') # 인덱싱
# print(t1[0])

# t1 = (1, 2, 'a', 'b') # 슬라이싱
# print(t1[1:])

# t1 = (1, 2, 'a', 'b')
# t2 = (3, 4)
# t3 = t1 + t2 # 새로운 튜플을 만드는 것
# print(t3)

t2 = (3, 4)
t3 = t2 * 3
print(t3)

# 튜플은 요솟값을 변경할수 없기 때문에 sort, insert, remove, pop과 같은 내장 함수가 없다.