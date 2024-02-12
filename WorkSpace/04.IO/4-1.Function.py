# def 함수_이름(매개변수):
#     수행할_문장1
#     수행할_문장2

def add(a, b): # 함수의 이름은 add이고 입력으로 2개의 값을 받으며
    return a + b # 리턴값(출력값)은 2개의 입력값을 더한 값이다
print(add(1,2))

# 매개변수(parameter) - 함수에서 정의되어 사용되는 변수(=인자, 파라미터)
# 인수(arguments) - 함수를 호출할 때 건네주는 변수
# a, b는 매개변수, 1, 2는 인수

def add(a, b): # 일반적인 함수
    result = a + b 
    return result

def say(): # 입력값이 없는 함수
    return 'Hi'
a = say()
print(a)

def add(a, b): # 리턴값이 없는 함수
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
add(1,2)

def say(): # 입력값도, 리턴값도 없는 함수
    print('Hi')
say()

def sub(a, b): # 매개변수를 지정하여 호출하기
    return a - b
result = sub(b=3,a=1)
print(result)

# def 함수_이름(*매개변수): 입력값이 몇 개가 될지 모를 때
#     수행할_문장
#     ...

def add_many(*args): # 여러 개의 입력값을 받는 함수
    result = 0 
    for i in args: 
        result = result + i   # *args에 입력받은 모든 값을 더한다.
    return result
print(add_many(1,2,3,4,5))

def add_mul(choice, *args): 
    if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
        result = 0 
        for i in args: 
            result = result + i 
    elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
        result = 1 
        for i in args: 
            result = result * i 
    return result
print(add_mul("mul", 1, 2, 3))

def print_kwargs(**kwargs): # 키워드 매개변수, kwargs
    # print(kwargs)
    print(kwargs['a'])
print_kwargs(a=1,b=2) # 딕셔너리 형태로 출력

# 함수의 리턴값은 언제나 하나이다
def add_and_mul(a,b): 
    return a+b, a*b
print(add_and_mul(3,4)) # 튜플값 하나인 (7, 12)로 리턴

def add_and_mul(a,b): 
    return a+b # return 만나면 함수가 종료됨
    return a*b # 실행 X

def say_nick(nick): 
    if nick == "바보": 
        return # "바보" 함수를 빠져나간다.
    print("나의 별명은 %s 입니다." % nick)
say_nick("야호")
say_nick("바보")

# 매개변수에 초깃값 미리 설정
def say_myself(name, age, man=True): # 초기화하고 싶은 매개변수는 뒤쪽에
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
say_myself("홍길동", 26)

# 함수 안에서 선언한 변수의 효력 범위
# a = 1 # 전역변수
# def vartest(a):
#     a = a +1 # 지역변수
# vartest(a)
# print(a)

# vartest_error.py
# def vartest(b):
#     b = b + 1
# vartest(3)
# print(b) # NameError: name 'b' is not defined

# 함수 안에서 함수 밖의 변수를 변경하기
a = 1 
def vartest(a): # return 사용하기
    a = a +1 
    return a
a = vartest(a) 
print(a)

a = 1 
def vartest(): # global 명령어
    global a # 함수 밖의 a 변수를 직접 사용하겠다는 뜻
    a = a+1
vartest() 
print(a)

# lambda 예약어
# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식
add = lambda a, b: a+b
result = add(3, 4)
print(result)
