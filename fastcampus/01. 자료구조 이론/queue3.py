import queue

data_queue = queue.PriorityQueue()

data_queue.put((10, "korea")) # 우선순위, 데이터 쌍으로 튜플
data_queue.put((5, 99))
data_queue.put((15, "china"))
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())