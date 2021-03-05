# 수의 사이사이 들어가야 하기 때문에 연산자는 n-1
# 연산자의 리스트의 수는 3 ^ n-1
from itertools import product

test_case = int(input())

for _ in range(test_case):
    operatiors_list = [" ", "+", "-"]
    n = int(input())
    operatiors_list = list(product(operatiors_list, repeat=n-1))
    integers = [i for i in range(1, n + 1)]

    for operatiors in operatiors_list:
        string = ""
        for i in range(n - 1):
            string += str(integers[i]) + operatiors[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()