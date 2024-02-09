# if 조건문: # 꼭 콜론 붙이기
#     수행할_문장1 # 꼭 들여쓰기, 안하면 오류
#     수행할_문장2
#     ...
# else:
#     수행할_문장A
#     수행할_문장B
#     ...

# 돈이 있으면 택시를 타고 가고, 돈이 없으면 걸어간다.
# money = True
# if money:
#     print("택시를 타고 가라") # True 일 때 실행
# else:
#     print("걸어 가라") # False 일 때 실행

# 비교 연산자 : <, >, ==, !=, >=, <=
x = 3
y = 2
print(x > y)

# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고, 아니면 걸어가라
money = 2000
if money >= 3000:
    print("택시 타라")
else:
    print("걸어 가라")

# and: x와 y 모두 참
# or : x와 y 둘 중 하나만 참이어도 참
# not x: x가 거짓이면 참

# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라
money = 2000
card = True
if money >= 3000 or card: # money는 2000이지만 card가 True니까 참
    print("택시 타라")
else:
    print("걸어 가라")

# in, not in
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c'))
print('j' not in "python")

# 만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시 타라")
else:
    print("걸어 가라")

# 조건문에서 아무 일도 일어나지 않게 설정 => pass
# 주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

# elif
# 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시 타라")
elif card:
    print("택시 타라")
else:
    print("걸어 가라")

# if문 한줄로
if 'money' in pocket: pass
else: print("걸어 가라")

# 조건부 표현식
score = 100
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)
# 변수 = 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값
message = "success" if score >= 60 else "failure"
