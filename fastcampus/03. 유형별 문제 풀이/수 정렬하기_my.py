num = int(input())
numbers = list()
for i in range(num):
    number = int(input())
    numbers.append(number)
numbers.sort()
for j in numbers:
    print(j)