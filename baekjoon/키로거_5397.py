testcase_num = int(input())
password = []

# 입력받은 개수만큼 반복
for i in range(testcase_num):
    # 커서의 왼쪽 스택, 오른쪽 스택을 초기화
    right, left = list(), list()
    # 비밀번호를 입력받는다.
    pass_input = input()
    # 비밀번호의 문자열을 하나씩 순회
    for char in pass_input:
        # 커서가 왼쪽으로 움직이므로, 오른쪽 스택에 한 문자가 더해진다.
        if char == "<":
            # 스택이 비어있지 않다면
            if left:
                right.append(left.pop())
        # 커서가 오른쪽으로 움직이므로, 왼쪽 스택에 한 문자가 더해진다.
        elif char == ">":
            # 스택이 비어있지 않다면
            if right:
                left.append(right.pop())
        # -이전의 문자가 지워지므로, 왼쪽 스택을 pop한다.
        elif char == "-":
            if left:
                left.pop()
        # 이외의 글자라면 lef에 append
        else:
            left.append(char)
    # 오른쪽에 append를 해왔기 때문에 반대로 저장되어 있다. 
    # reversed로 역정렬해 왼쪽 스택과 더해준다.
    left.extend(reversed(right))
    print("".join(left))