"""
1. 자료형
1-1 숫자
10+5
(10-5) * 2
10/2
=> 파이썬에서는 소수점을 사용하지 않는 경우 기본적으로 int로 처리

2.2 * 5
1.0/0.2
3/2
=> 파이썬에서는 소수점을 사용하거나 계산 결과가 실수인 경우 float으로 처리

3/2
3//3
5%2
=> / float // int % 나머지

2 ** 5
2 ** 10
=> ** 거듭제곱

a = 10
b = 20
a * b

1-2. 문자열
msg = 'hello'
msg2 = "HELLO"
msg3 = '"Nice to meet you", chatbot says'
msg
msg2
msg3
msg4 = 'Hello \n kgy'
msg4
msg5 = '''Hello
... kgy!!'''
msg5
print(msg5)
=> 멀티라인 문자열은 \n 쓰거나 ''' ... 사용

1-3. 리스트
numbers = [1,2,3,4,5]
numbers[1]
numbers[-1]
numbers[2:]
numbers[1:-2]
numbers[-2:]
=> 리스트 인덱싱 또는 슬라이싱(슬라이싱은 새로운 배열으로 반환)
numbers[0] = 10
=> 리스트 요소 변환
numbers.append(9)
=> 리스트 마지막에 추가
numbers.insert(1,8)
=> 리스트 원한는 위치에 추가
numbers.pop(2)
=> 리스트 꺼내고 삭제
del numbers[2]
=> 리스트 그냥 삭제
len(numbers)
=> 리스트 길

1-4. 튜플
numbers = (1,2,3,4,5)
numbers[0]
numbers[:2]
=> 리스트 하지만 한번 생성하면 순서 내용 수정 X, 인덱싱 슬라이싱 제공

1-5. 딕셔너리
user = {'name':'홍길동', 'age':30}
user['name']
=> key value 가지고 있음 map이라 생각하면

1-6. 불리언
check = True
uncheck = False
=> 첫 문자는 대문자

=====================================================================

2. 제어문
2-1. if 조건문
"""
check = True
if check:
 print('check is True')
else:
 print('check is False')

check = False
if not check:
 print('check is False')
else:
 print('check is True')

age = 15
if age < 20:
 print('미성년자입니다.')
else:
 print('성년입니다.')

"""
2-2. while 반복문
"""
i = 1
while i < 10:
     print(i)
     i = i + 1
     
"""
2-3. for 반복문
for 변수 in 리스트|튜플|문자열
   코드
   코드
"""
numbers = [1,2,3,4,5]
for n in numbers:
    print(n)

numbers = range(1,6)
for n in numbers:
    print(n)