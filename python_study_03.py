'''
5. 모듈
- 여러가지 함수나 클래스 등을 기능이나 목적별로 모아놓은 파일
- 공개된 여러 파이썬 모듈을 사용 가능
- 직접 만드는 방법? : calc.py 참

- import 키워드를 이용하여 모듈을 사용한다.

import calc

a = calc.add(10, 20)
print(a)
b = calc.mul(10, 2)
print(b)

- 모듈명 없이 함수명으로 사용하고 싶을 경우 from, import 키워드를 사용한다.
'''
from calc import add, mul

a = add(10, 20)
print(a)
b = mul(10, 2)
print(b)

'''
- 다음과 같이 *를 이용해서 모든 함수를 모듈에서 불러올 수 도 있다.
from calc import *

- 모듈은 함수만 포함하는 것이 아니라 변수, 클래스 또한 포함할 수 있다.고 : module.py 참

import module
print(module.PI)
c = module.Math() #모듈 안에 있는 Math 클래스로 객체 생성
print(c.slov(2))

6. 예외 처리
- 파이썬에서는 예외 처리를 위해 try-except 구문을 문법적으로 사용한다.
try:
 ...
except 오류상항 as 오류 메시지 변수:
 ...
finally:
 ...  
'''
try:
  a = 10
  b = 0
  c = a / b #0으로 나눌 수 없다
  print(c)
except Exception as e:
  print(e)

