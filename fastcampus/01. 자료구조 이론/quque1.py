import queue

data_queue = queue.Queue()
data_queue.put("coding")
data_queue.put(99)
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())