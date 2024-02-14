# 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일

# 모듈 불러오기
import mod1 # import: 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해 주는 명령어
print(mod1.add(3,4))

# from 모듈_이름 import 모듈_함수
from mod1 import * # * 전체
print(add(3,4))

import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))

# 다른 디렉터리에 있는 모듈을 불러오기
import sys
sys.path.append("D:/Study_Python/WorkSpace")
import mod3
a = mod3.Math()
print(a.solv(2))