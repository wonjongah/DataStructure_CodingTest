testcase_num = int(input())
password = []

for i in range(testcase_num):
    right, left = list(), list()
    pass_input = input()
    
    for char in pass_input:
        if char == "<":
            if left:
                right.append(left.pop())
        elif char == ">":
            if right:
                left.append(right.pop())
        elif char == "-":
            if left:
                left.pop()
        else:
            left.append(char)
    left.extend(reversed(right))
    print("".join(left))