n = int(input())

stack = []
result = []
count = 1

# 숫자만큼 반복
for i in range(n):
    input_num = int(input())
    # 입력받은 수까지 숫자를 늘려가며 stack에 쌓는다
    while count <= input_num:
        stack.append(count)
        count += 1
        result.append("+")
    # 만일 stack의 마지막 원소가 입력한 숫자와 같다면 pop
    if stack[-1] == input_num:
        stack.pop()
        result.append("-")
    # while에 들어가지도 못하고, stack의 마지막 원소가 입력한 숫자가 아니라면
    # NO 출력하고 종료
    else:
        print("NO")
        exit(0)

for j in result:
    print(j)