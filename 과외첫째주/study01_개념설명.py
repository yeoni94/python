"""
==============파이썬 함수 개념 설명==============
1. 함수란? 프로그램에서 자주 사용되는 코드를 따로 만들어 필요할때마다 호출해서 사용하는 기능
2. 내장 함수
  파이썬은 기본적으로 자주 사용하는 기능을 함수로 만들어 놓고 제공하고 있다.
  즉 파이썬을 설치하면 기본 셋팅된 함수들을 내장함수라고 한다.

  입력함수
  input('input the number:')

  출력함수
  print('hello word!')

  형변환 함수
  int('12')
  str(31)
  float(15)

  랜덤함수
  random.randint(1,20)

3. 사용자정의함수
  내장함수에 내가 원한 기능이 없을 경우 사용자가 직접 함수를 만들어 사용할 수 있다.

  for문을 사용해서 1부터 10까지 더한 합을 출력할 경우?
"""
summation = 0

for i in range(1, 11):
    summation += i
print('1~10 합은 %d' %summation)

#for문을 사용해서 1부 100까지 더한 합을 출력할 경우?
summation = 0

for i in range(1, 101):
    summation += i
print('1~100 합은 %d' %summation)

"""
이런식으로 비슷한 코드인데 매번 사용할때마다 작성하는 것은 비효율적!
따라서 이를 함수로 만들어 놓고(이를 사용자정의함수라고한다) 해당 함수를 호출해서 사용하는 것이 효율적이다. 
"""
def num_sum(x):
    summation = 0

    for i in range(1, x+1):
        summation += i
    print('1~%d 합은 %d' %(x, summation))

num_sum(10)
num_sum(100)
num_sum(1000)

"""
4. 함수 정의파트, 호출파트
먼저 함수를 사용하기 위해서는 함수를 작성해야 한다. 이를 함수 정의 라고 한다.
"""
def bird () :
    print('새가 짹짹짹')

#정의한 함수는 호출해서 사용할 수 있다. 호출 방법은 함수명() 이렇게 작성하면 된다.
bird()

#함수 정의시 매개변수 parameter를 입력하여 함수 안에서 사용할 값을 함수 호출때마다 다른 값으로 설정가능하게 한다.
def f(x):
    print(2*x+1)

#매개변수가 사용된 함수를 호출할 경우 인수 arguments를 사용해야 한다.
f(10)

#단순히 함수를 실행하는 것이 아니라 함수의 실행 결과로 값을 반환하고 싶을 경우 'return' 키워드를 사용한다.
def f2(x):
    return 2*x+1
result = f2(10)
print(result)

"""
5. 함수의 형태
입력값 = 매개변수
결과값 = return

입력값 o, 결과값 o
"""
def add(a,b):
    sum = a+b
    return sum

result = add(3,4)
print(result)

"""
입력값 x, 결과값 o
"""
def say():
    return 'Hello'

result = say()
print(result)

"""
입력값 o, 결과값 x
"""
def add(a,b):
    sum = a+b
    print('%d, %d의 합은 %d입니다.' %(a, b, sum))
add(3, 4)
"""
return 키워드가 없을 경우 None 을 반환
"""
result = add(3, 4)
print(result)

"""
입력값 x, 결과값 x
"""
def say():
    print('Hello')

say()

"""
6. 지역변수와 전역변수
지역변수 = 함수 안에 정의된 변수
전역변수 = 함수 밖에 정의된 변수

똑같은 이름으로 변수가 정의되어 있을 경우 지역변수가 우선이다.
"""
a = 0 #전역변수

def print_test():
    a = 10 #지역변수
    b = a + 10
    print(b)

print_test()

"""
그렇다면 전역변수를 함수 안에서 사용하고 싶을경우 global 키워드를 사용한다.
"""
a = 0

def print_test():
    global a
    a += 1
    b = a + 10
    print(b)

print_test()

"""
7. 여러개 입력값 함수

입력값을 여러개 받고 싶을 경우? 매개변수 앞에 *를 붙인다. 이를 가변 매개변수(튜플형)라고 한다.
"""
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

result1 = add_many(1,2,3)
print(result1)
result2 = add_many(1,2,3,4,5,6,7,8,9,10)
print(result2)

"""
일반 매개변수와 가변 매개변수를 동시 사용 가능하다.
"""
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
        return result
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
        return result

result1= add_mul('add',1,2,3,4,5)
print(result1)
result2= add_mul('mul',1,2,3,4,5)
print(result2)

"""
단순 리스트 형태의 매개변수가 아니라 key와 value로 데이터를 받고 싶을경우 매개변수 앞에 **를 붙인다.
이를 사전형 가변 매개변수라고 한다.
"""
def test(**kwargs):
    print(kwargs)

test(a=1, b=2, c=3)
test(name='홍길동', age=28, tel='010-1111-1111')

def test(**kwargs):
    if kwargs.get("name") == '홍길동':
        print('홍길동님 안녕하세요.')
test(name='홍길동', age=28, tel='010-1111-1111')

"""
8. map() 함수
기존 리스트를 함수에 넣고 새로 리턴받은 새로운 값을 모아서 리스트로 줌
"""
def mul(item):
    return item * item

list_a = [1,2,3,4,5]

output1 = map(mul,list_a)
print(list(output1))

"""
9. filter() 함수
기존 리스트를 함수에 넣고 함수 안에 설정한 조건에 맞는 즉 true로 반환되는 값을 모아서 리스트로 줌
"""
def under_3(item):
    return item < 3

list_a = [1,2,3,4,5]

output1 = filter(under_3, list_a)
print(list(output1))

"""
10. 람다 lamba
함수 구문을 좀더 간단하게 작성할 수 있는 방법
함수 안 코드가 적을 경우 사용
"""
add = lambda a, b : a + b #람다로 함수를 간단히 작성
result = add(3,4)
print(result)

"""
람다를 한개만 작성하는 것이 아니라 여러개를 작성해서 리스트에 담아두고 
필요할때 여러개의 람다 중에 특정 람다를 꺼내서 사용할 수 있다.
"""
make_file = [lambda x : x + '.pptx', lambda x : x + '.docx']

homework1 = make_file[0]('피피티발표')
print(homework1)

homework2 = make_file[1]('문서발표')
print(homework2)

"""
람다는 filter 함수 안에서도 사용 가능하다.
다음은 양수만 출력하는 예제이다.
"""
list_a = [1,-1,-2,3,0,-5,8]
positive_func = filter(lambda x : x>0 , list_a)
print(list(positive_func))

"""
람다는 map 함수 안에서도 사용 가능하다.
다음은 주어진 리스트의 값을 제곱을 해서 다시 리스트로 반환하는 예제이다.
"""
list_a = [1,2,3,4,5]
mul_func = map(lambda x:x*x, list_a)
print(list(mul_func))

"""
람다의 매개변수를 여러개 설정할 수도 있다.
"""
list_a = [1,2,3,4,5]
list_b = [6,7,8,9,10]
mul_func = map(lambda x,y : x + y, list_a, list_b)
print(list(mul_func))

"""
람다를 사용해서 다음 리스트의 홀수만 추출해라
"""
numbers = list(range(1,11))
odd = list(filter(lambda x:x%2==1, numbers))
print(odd)

"""
람다를 사용하여 다음 리스트의 3이상 7미만을 추출해라
"""
numbers = list(range(1,11))
num1 = list(filter(lambda x:x>=3 and x<7, numbers))
print(num1)

"""
람다를 사용해서 다음 리스트의 값을 제곱해서 50 미만을 추출해라
"""
num2 = list(filter(lambda x:x**2 < 50, numbers))
print(num2)