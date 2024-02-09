test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first,last) in a:
    print(first+last)

# 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격
score = [90, 25, 67, 45, 80]
number = 0
for i in score:
    number += 1
    if i >= 60:
        print("%d번 학생은 합격" %number)
    else:
        print("%d번 학생은 불합격" %number)

# 60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무런 메시지도 전하지 않는 프로그램
score = [90, 25, 67, 45, 80]
number = 0
for i in score:
    number += 1
    if i < 60:
        continue
    else:
        print("%d번 학생 축하드립니다. 합격입니다." %number)

# range 함수
add = 0
for i in range(1, 11): # 1이상 11미만
    add += i
print(add)

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ") # end 파라미터 다음 줄로 넘기지 않고 계속 출력
    print('')

a = [1,2,3,4]
result = [num*3 for num in a]
print(result)
