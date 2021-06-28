num = input()
num = list(map(int, list(num)))
num.sort(reverse=True)
for i in num:
    print(i, end="")