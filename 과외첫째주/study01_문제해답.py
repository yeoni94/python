"""
1. 내장함수 random의 randint를 사용하여 1~100 사이의 임의의 정수를 출력해라
(내장함수 관련 문제)
"""
import random

num = random.randint(1,100)
print(num)

"""
2. 매개변수 2개 x,y를 셋팅하여 두개의 합을 리턴해주는 add 함수를 생성하고 이를 출력해라
(입력값 o, 결과값 x 관련 문제)
"""
def add(x,y):
    return x+y

print(add(1,5))

"""
3. '안녕하세요' 문자열을 리턴하는 hello라는 이름의 함수를 생성하고 이를 변수 result에 담아 출력해라
(입력값 x, 결과값 o 관련 문제)
"""
def hello():
    return '안녕하세요'

result = hello()
print(result)

"""
4. 매개변수 2개 a,b를 셋팅하여 두개의 곱을 출력하는 mul이라는 이름의 함수를 생성하고 이를 호출해라.
(입력값 o, 결과값 x 관련 문제)
"""
def mul(a,b):
    print(a * b)
mul(1,5)

"""
5. 단순히 '테스트 진행 중입니다.' 문자열을 출력하는 test라는 이름의 함수를 생성하고 이를 호출해라
(입력값 x, 결과값 x 관련 문제)
"""
def test():
    print('테스트 진행 중입니다.')
test()

"""
6. 전역변수 a에 10을 셋팅하고 함수 안에서 전역변수 값을 20으로 변경하고 변경된 값을 출력하는 print_test라는 이름의 함수를 생성하고 이를 호출해라
"""
a = 10
def print_test():
    global a
    a = 20
    print(a)
print_test()

"""
7. 튜플형 가변 매개변수를 가지고 있는 add_all 이라는 이름의 함수를 작성해라.
   add_all 함수는 매개변수로 들어온 값을 반복해서 한개씩 출력하도록 작성하고 이를 호출해라.
"""
def add_all(*args):
    for i in args:
        print(i)
 
add_all(1,2,3,4,5)

"""
8. map() 함수를 이용해서 다음 리스트의 값에 2를 더한 값으로 새로운 리스트를 만들어서 출력해라
- 새로운 리스트 이름은 list_b
- 함수를 사용한 방법으로 1개 작성 함수 이름은 add_2
- 람다를 사용한 방법으로 1개 작성
list_a = [1,2,3,4,5]
"""
#함수 사용
list_a = [1,2,3,4,5]
def add_2(i):
    return i+2

list_b = map(add_2, list_a)
print(list(list_b))

#람다 사용
list_a = [1,2,3,4,5]
list_b = map(lambda i:i+2, list_a)
print(list(list_b))

"""
9. filter() 함수를 이용해서 다음 리스트의 값이 10보다 작은 경우의 값으로 새로운 리스트를 만들어서 출력해라
- 새로운 리스트 이름은 list_b
- 함수를 사용한 방법으로 1개 작성 함수 이름은 check_10
- 람다를 사용한 방법으로 1개 작성
list_a = [1,5,10,15,20]
"""
list_a = [1,5,10,15,20]
def check_10(i):
    return i<10
list_b = filter(check_10,list_a)
print(list(list_b))

"""
10. 1부터 15까지의 임의의 정수를 하나 만들고 7번의 기회로 정수를 맞춰보세요.
- 입력한 값이 임의의 정수보다 클 경우 '입력한 값은 너무 큽니다.'를 출력
- 입력한 값이 임의의 정수보다 작을 경우 '입력한 값은 너무 작습니다.'를 출력
- 값을 맞추었을 경우 '축하합니다. 값을 맞췄습니다.'를 출력
- 기회를 모두 소진했을 경우 '7번 기회를 모두 소진했습니다.'를 출력
"""
import random
hit = 0
com = random.randint(1,15)
for i in range(7):
    you = int(input('1~15 사이의 정수를 입력하세요!'))
    if you > com:
        print('입력한 값은 너무 큽니다.')
    elif you < com:
        print('입력한 값은 너무 작습니다.')
    else:
        print('축하합니다. 값을 맞췄습니다.')
        break
    hit += 1
    if hit == 7:
        print('7번 기회를 모두 소진했습니다.')

"""
11. {'a':2,'b':3,'c':2,'d':1} 과 같이 출력되도록 문자열 'a', 'b', 'c' , 'd' 를 가지고 있는 리스트를 만들고
해당 문자열이 몆번 등장하는지 출력하는 프로그램을 작성해라
"""
list_abcd = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'd']
counter = {}

for i in list_abcd:
    if i not in counter:
        counter[i] = 1
    else:
        num = counter.get(i)
        counter[i] = num + 1
print(counter)