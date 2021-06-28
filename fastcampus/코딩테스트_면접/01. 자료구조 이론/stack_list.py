stack_list = list()


def push(data):
    stack_list.append(data)

def pop():
    poped_data = stack_list[-1]
    del stack_list[-1]
    return poped_data

push(1)
push(2)
push(3)
print(stack_list)
print(pop())
print(pop())
print(stack_list)