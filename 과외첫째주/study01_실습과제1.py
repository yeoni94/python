"""
1부터 10까지의 임의의 정수를 하나 만들고, 5번의 기회로 정수를 맞춰보세요.
(임의의 정수는 randint 함수를 사용함)
"""
import random
hit = 0
com = random.randint(1,10)
for i in range(5):
    you = int(input('1~10 사이의 정수를 입력하세요!'))
    if you > com :
        print('당신이 선택한 숫자는 큽니다.')
    elif you < com :
        print('당신이 선택한 숫자는 작습니다.')
    else:
        print('정답!!!!')
        break
    hit+=1
    if hit == 5:
        print('5번 기회 모두 소진 ㅋㅋㅋㅋ')