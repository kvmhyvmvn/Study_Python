# 파일_객체 = open(파일_이름, 파일_열기_모드)
# 파일열기모드: r 읽기, w 쓰기, a 추가
# f = open("filetest/새파일.txt", 'w')
# f.close()

# f = open("D:/Study_Python/filetest/새파일2.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("새파일.txt", 'w', encoding="UTF-8")
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f = open("D:/Study_Python/filetest/새파일2.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# while True:
#     data = input()
#     data = int(data)
#     if not data: break
#     print(data)

# f = open("D:/Study_Python/filetest/새파일2.txt", 'r')
# lines = f.readlines() # list 형태로 리턴
# for line in lines:
#     line = line.strip() # 줄바꿈(\n) 제거(replace도 가능)
#     print(line)   
# f.close()

# f = open("D:/Study_Python/filetest/새파일2.txt", 'r')
# data = f.read() # 파일 내용 전체->문자열로 리턴
# print(data)
# f.close()

# f = open("D:/Study_Python/filetest/새파일2.txt", 'r')
# for line in f:
#     print(line)
# f.close()

# 쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다.
# 새로운 값만 추가해야 할 경우 파일을 추가 모드('a')로 열기
f = open("D:/Study_Python/filetest/새파일2.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

# close 자동
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
