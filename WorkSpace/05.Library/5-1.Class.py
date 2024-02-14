# 반복되는 변수, 메소드(함수)를 미리 정해놓은 틀(설계도)

# 계산기의 '더하기' 기능을 구현
# result = 0
# def add(num):
#     global result
#     result += num # 결괏값(result)에 입력값(num) 더하기
#     return result # 결괏값 리턴
# print(add(3))
# print(add(4))

# # 계산기의 개수와 기능이 추가된다면?
# class Calculator:
#     def __init__(self):
#         self.result = 0
    
#     def add(self, num):
#         self.result +=  num
#         return self.result
    
# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

class Cookie: # 맨 앞글자는 대문자로
    pass

a = Cookie() # Cookie라는 클래스의 객체(인스턴스)를 만든다.
b = Cookie() # Cookie의 결괏값을 리턴받은 a, b가 객체(인스턴스)이다.

# class FourCal:
#     def setdata(self, first, second): # self에는 setdata 메서드를 호출한 객체 a가 자동으로 전달
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second # 4 + 2
#         return result # 6
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal()
# a.setdata(4,2)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())

# b = FourCal()
# b.setdata(10,5)
# print(b.add())
# print(b.sub())
# print(b.mul())
# print(b.div())

# 생성자: 객체가 생성될 때 자동으로 호출되는 메소드(__init__)
# FourCal 클래스의 인스턴스 a에 setdata 메소드를 수행하지 않고 add 메소드를 먼저 수행하면
# ‘AttributeError: 'FourCal' object has no attribute 'first'’오류가 발생한다.
# 객체에 초깃값을 설정해야 할 필요가 있을 때는 생성자를 구현하는 것이 좋다.

class FourCal:
    def __init__(self, first, second): # 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다.
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
print(a.add())
print(a.mul())

# 상속(Inheritance) class 클래스_이름(상속할_클래스_이름)
class MoreFourCal(FourCal):
    def pow(self): # 제곱
        result = self.first ** self.second
        return result
    
a = MoreFourCal(4,2)
print(a.add())
print(a.pow())

# 메소드 오버라이딩: 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)
print(a.div())

# 클래스 변수
class Family:
    lastname = "김"

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
