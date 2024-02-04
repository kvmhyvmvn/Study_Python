# a = "Life is too short, You need Python"
# b = "a"
# c = "123"
# print(type(a))

# a = "I\'m Hungry"
# print(a)

# a = "Life is too short\nYou need Python"
# print(a)
# b = """Life is too short
# You need Python"""
# print(b)
# c = "Life is too short\tYou need Python"
# print(c)

# head = "Python"
# tail = " is fun!"
# print(head + tail)
# print(head*3)

# # multistring.py
# print("=" * 50)
# print("My Program")
# print("=" * 50)

# # a = "Life is too short, You need Python"
# print(len(a)) # 문자열 길이

# # 인덱싱
# print(a[0])
# print(a[12])
# print(a[-1])

# # 슬라이싱
# print(a[0:4]) # 0이상 4미만
# print(a[19:]) # 미만이 없다 => 끝까지 출력
# print(a[::2]) # 이상:미만:간격 처음부터 끝까지 2칸 간격으로 출력
# print(a[::-1]) # 거꾸로
# print(a[19:-7])

# a = "20240205Rainy"
# date = a[:8]
# weather = a[8:]
# print(date)
# print(weather)

# a = "I eat %d apples" %3 # 숫자 대입
# b = "I eat %s apples" % "three" # 문자 대입
# print(a)
# print(b)

# number = 10
# day = "three"
# a = "I ate %d apples. So I was sick for %s days." %(number, day)
# print(a)
# b = "I ate {0} apples. So I was sick for {1} days." .format(number, day)
# print(b)
# c = f"I ate {number+1} apples. So I was sick for {day} days."
# print(c)

# a = "%0.4f" % 3.42134234 # 소숫점 4번째까지 출력
# print(a)
# b = 3.42134234
# b = f'{b:0.4f}'
# print(b)

a = " hobby "
print(a.count('b')) # b 개수
print(a.find('o')) # o 위치(인덱스), 없는 값 넣으면 -1
print(a.index('o')) #               없는 값 넣으면 오류
print(a.lstrip()) # 공백제거(l 왼쪽 r 오른쪽)

# a = ", ".join('abcd') # 문자 사이에 ', ' 삽입
# print(a)
# print(a.upper()) # 대문자


# r = "Life is short."
# print(r.replace("Life", "Your leg")) # Life 자리에 Your leg 삽입
# print(r.split())