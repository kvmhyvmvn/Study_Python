# 참(True), 거짓(False) 첫 문자를 항상 대문자로 작성
a = True
b = False
print(type(a))
print(type(b))

print(1==1)
print(1==2)
print(1<2)
print(1>2)

# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면("", [], (), {}) 거짓이 되고 비어 있지 않으면 참이 된다.
# 숫자에서는 그 값이 0일 때 거짓이 된다.
# None 거짓을 뜻한다.

print(bool("python"))
print(bool(''))