"""
{1:3,2:5,3:2,8:3,5:2,6:2,9:2,7:2,4:2}
위와 같이 출력되도록 numbers 내부에 숫자가 몇 번 등장하는지 출력하는 프로그램을 작성해라
"""
numbers = [1,2,3,8,5,2,2,1,8,3,6,9,7,2,4,4,6,8,1,2,5,7,9]
counter = {}
for i in numbers:
    if i not in counter:
        counter[i] = 1 #key 셋팅과 동시에 초기 value를 1로 셋팅
    else:
        num = counter.get(i)
        counter[i] = num + 1 #value 값을 추가
print(counter)