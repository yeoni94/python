'''
3. 함수
- 하나의 기능을 수행하는 코드들의 집합
- 반복적으로 수행하는 코드들을 기능 단위로 묶어서 재사용
- 입력값 + 결과값

3-1. 사용자 정의 함수
- 사용자가 직접 만든 함수
'''
def add(a, b):
    return a + b
result = add(10, 20)
print(result)

def print_user(user, score):
    print('%s님의 성적은 %d점 입니다.' % (user,score))
print_user('김가연', 90)

'''
3-2. 내장 함수
- 파이썬 시스템에 기본적으로 내장되어 있는 함수
- format() : 문자열 포매팅 함수, {} 중괄호와 순서에 맞는 인덱스만 사용하면 됨
'''
print('integer : {} / float : {} / string : {}'.format(10, 3.14, "hello"))

'''
- enumerate() : 순서 있는 자료형을 입력시 인덱스 포함한 요솟값 반환
'''
numbers = [1,2,3,4,5]
for idx, value in enumerate(numbers):
    print('index : {}, value : {}'.format(idx, value))

'''
- str() : 입력으로 들어온 값을 문자열로 반환
'''
print(type(str(10)))

'''
- join() : 리스트 요소들을 구분자로 구분해 문자열로 반환
'''
name = ['홍길동', '김영희', '이철수']
names = ','.join(name)
print(names)

'''
- split() : 문자열을 특정 구분자로 구분해 리스트로 반환
'''
name_split = names.split(',')
print(name_split)

'''
- id() : 객체를 입력받아 객체의 고유 주솟값(래퍼런스) 반환
'''
a = 10
print(id(a))

'''
- find() : 특정 문자열을 위치 찾기 위해 사용하는 함수, 시작 위치 반환, 없을 경우 -1 반환
'''
str = "I want to be a great programmer"
print(str.find("be"))
print(str.find("ae"))

'''
- strip() : 주어진 문자열 양쪽 끝 공백 제거
'''
msg = " test "
print(msg)
print(msg.strip())

'''
- filter() : 반복적 셀수 있는 객체 입력 받아 특정 함수로 수행 후 결과 값이 true인 것만 반환
'''
def is_even(number):
    return number % 2 == 0
numbers2 = range(1,21)
even_list = list(filter(is_even, numbers2))
print(even_list)

'''
3-3. 외장 함수
- 파이썬 라이브러리에서 함수를 가져다 쓰는 것
- 클래스와 모튤 형태로 묶여 있음
- import 키워드 사용해서 해당 모듈 불러와야 함

기본적으로 제공하는 표준 라이브러리의 외장 함수는 다음과 같

- sys : 파이썬 인터프리터와 관련된 정보와 기능을 제공하는 모듈
- pickle : 파이썬 객체를 파일로 저장하고 메모리로 읽어올 수 있도록 도와주는 모듈
- time : 시스템이 제공하는 시간과 관련된 유용한 함수들을 포함
- random : 난수값을 생성하는 기능과 다양한 랜덤 관련 함수를 제공다

해당 외장 함수는 필요한 경우 검색해서 사용하자

4. 클래스
- 객체 지향 언어에서는 객체를 생성하기 위해 클래스를 제공
- 파이썬도 객체 지향 언어임으로 클래스 제공
- 파이썬에서 사용하는 모든 자료형은 객체
- 객체? 데이터 상태와 동작 행위를 가지고 있는 코드 그룹
- 클래스를 이용해 객체 생성
'''
#챗봇 클래스
class Chatbot :
    def sayHello(self):
        print("say hello")

    def sayMyName(self):
        print("My name is kkk")

#챗봇 인스턴스 생성
chatbot = Chatbot()
chatbot.sayHello()
chatbot.sayMyName()

#생성자 : 객체가 생성될 때 자동으로 호출되는 메서드
#소멸자 : 객체가 소멸될 때 자동으로 호출되는 메서드
class Test :
    def __init__(self):
        print("객체가 생성됩니다.")
    def __del__(self):
        print("객체가 소멸됩니다.")

test = Test()
print("123456789")
del test

#클래스는 매서드와 인스턴스 변수로 구성되어 있다. 인스턴스 변수는 self 키워드를 붙여 선언한다.
class Calc: #사칙 연산 클래스
    def __init__(self, init_value):
        self.value = init_value
    def add(self, n):
        return self.value + n
    def sub(self, n):
        return self.value - n
    def mul(self, n):
        return self.value * n
    def div(self, n):
        return self.value / n

cal = Calc(100)
print("value = {0}".format(cal.value))

a = cal.add(100)
b = cal.sub(50)
c = cal.mul(2)
d = cal.div(2)

print("a={0}, b={1}, c={2}, d={3}".format(a,b,c,d))

