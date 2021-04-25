"""
1. while문을 사용해서 '안녕하세요' 문자열을 10번 출력하세요.
"""
count = 0
while count < 10:
    print('안녕하세요.')
    count+=1

"""
2. 1부터 7까지의 정수를 for 반복문으로 출력하세요.
"""
for i in [1,2,3,4,5,6,7]:
    print(i)

"""
3. range 함수를 사용해서 범위를 1부터 10까지 셋팅한 for 반복문을 작성하세요.
반복문 안에서 'hello' 문자열을 출력하세요.
"""
for i in range(1,11):
    print('hello')

"""
4. 1부터 100까지 더하고 출력하기(range, for 사용)
"""
sum = 0
for i in range(1,101):
    sum += i
print(sum)

"""
5. 'hello' 문자열을 한개씩 출력하기
"""
text = 'hello'
for i in text:
    print(i)

"""
6. 1부터 15까지의 수에서 10미만을 출력하기
"""
for i in range(1,16):
    if i>9:
        break
    print(i)

"""
7. 1부터 100미 수에서 10의 배수만 출력하기
10,20,30,40,50,60,70,80,90 출력되어야함
"""
for i in range(1,100):
    if i%10 != 0:
        continue
    print(i)

"""
8. [10,20,30,40,50] 리스트를 다음과 같이 출력할 수 있는 코드를 작성하세요.
(for, enumerate 이용)

0번째 값은 10입니다.
1번째 값은 20입니다.
2번째 값은 30입니다.
3번째 값은 40입니다.
4번째 값은 50입니다.
"""
a_list = [10, 20, 30, 40, 50]
for i, value in enumerate(a_list):
    print('%d번째 값은 %d입니다.' %(i, value))