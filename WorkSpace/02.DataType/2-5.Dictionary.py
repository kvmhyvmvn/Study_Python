# 연관 배열(associative array), 해시(hash)
# {Key1: Value1, Key2: Value2, Key3: Value3, ...}

# dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# print(type(dic))
# print(dic)

# a = {'a': [1, 2, 3]} # value에 list 삽입 가능

# a = {1: 'a'}
# a[2] = 'b'
# print(a)
# a['name'] = 'pey'
# print(a)
# a[3] = [1, 2, 3]
# print(a)
# del a[1] # 삭제할 요소의 key 선택
# print(a)

# grade = {'pey': 10, 'julliet': 99}
# print(grade['pey'])

# dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
# print(dic['name'], dic['phone'])

# a = {1:'a', 1:'b'}
# print(a) # key 값이 같으면 하나를 제외한 나머지 것들은 무시된다.

# Key에 리스트는 쓸 수 없다. (변형가능 자료는 사용 불가, 튜플은 사용 가능)

# a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# print(a.keys()) # 딕셔너리 a의 Key만을 모아 dict_keys 객체를 리턴
# print(a.values())
# print(a.items())
# a.clear() # 딕셔너리 안 모든 요소 삭제
# print(a)

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name')) # 없는 key 넣으면 none
print(a.get('hi', "값이 없습니다.")) # 값이 없으면 "값이 없습니다." 출력
print('name' in a) # True
print('hi' in a) # False