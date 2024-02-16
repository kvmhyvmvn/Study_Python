# f = open("없는파일", 'r') # FileNotFoundError
# print(4 / 0) # ZeroDivisionError
# a = [1, 2, 3]
# print(a[3]) # IndexError

# try-except
try:
    4 / 0 # 오류가 발생할 수 있는 구문
except ZeroDivisionError as e:
    print(e) # 오류 출력

# try-finally
try:
    f = open("foo.txt", 'w')
    # 무언가를 수행한다.
finally:
    f.close() # 중간에 오류가 발생하더라도 무조건 실행된다.

# 여러개의 오류
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
# 인덱싱 오류가 먼저 발생했으므로 ZeroDivisionError 오류는 발생하지 않는다.

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# try-else
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else: # 오류가 발생하지 않았을 경우에만 수행
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

# 오류 회피
try:
    f = open("없는파일", 'r')
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기 => raise 명령어
# Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우
class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    # pass # fly 메소드 오버라이딩 X => NotImplementedError
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

class MyError(Exception):
    def __str__(self): # __str__: 오류 메시지를 print 문으로 출력할 경우에 호출되는 메소드
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)