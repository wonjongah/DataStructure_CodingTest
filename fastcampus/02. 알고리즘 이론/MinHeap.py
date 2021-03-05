import heapq

queue = []

heapq.heappush(queue, [2, 'A'])
heapq.heappush(queue, [5, 'B'])
heapq.heappush(queue, [1, 'C'])
heapq.heappush(queue, [7, 'D'])

# 맨 앞에 있는 요소가 제일 작은 요소가 되었다.
print(queue)

for index in range(len(queue)):
    print(heapq.heappop(queue))
    # 거리가 작은 순으로 뽑아낸다.