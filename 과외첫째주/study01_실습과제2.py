"""
두개의 정수를 입력받아 숫자 사이의 모든 수의 합을 구해보세요.
"""
num1 = int(input('정수를 입력하세요:'))
num2 = int(input('정수를 입력하세요:'))
sum = 0
for i in range(num1, num2+1):
    sum+=i
print('총합:',sum)
