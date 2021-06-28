n = int(input())

stack = []
result = []
count = 1

for i in range(n):
    input_num = int(input())
    # 입력한 수에 도달할 때까지 삽입
    while count <= input_num:
        stack.append(count)
        count += 1
        result.append("+")
    # 같을 때만 뽑기
    if stack[-1] == input_num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

# for j in result:
#     print(j)
print("\n".join(result))