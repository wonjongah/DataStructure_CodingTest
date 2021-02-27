queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    # data = queue_list[0]
    # del queue_list[0]
    # return data
    return queue_list.pop(0)

enqueue(3)
enqueue(4)
enqueue(5)
print(queue_list)
print(dequeue())
print(queue_list)
