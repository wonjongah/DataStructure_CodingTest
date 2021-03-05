n = int(input())

stack = []
result = []
count = 1

for i in range(n):
    input_num = int(input())
    while count <= input_num:
        stack.append(count)
        count += 1
        result.append("+")
    if stack[-1] == input_num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

for j in result:
    print(j)