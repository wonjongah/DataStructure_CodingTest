import heapq

def dijkstra(graph, start):
    # 각 키를 가져와서 키 : inf를 저장
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    queue = []

    # 첫 노드를 [0, 첫노드]로 초기화
    heapq.heappush(queue, [distances[start], start])

    # 우선순위 큐에 요소가 없을 때까지
    while queue:
        # 현재 거리가 가장 작은 요소를 큐에서 pop해서 현재 거리, 현재 노드에 저장 
        current_distance, current_node = heapq.heappop(queue)

        # 기존의 값이 더 작으면 밑의 작업을 할 필요가 없다.
        if distances[current_node] < current_distance:
            continue

        # 뽑힌 노드의 값에 연결된 노드들을 각각 저장
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            # 첫 노드와 연결된 노드와의 거리가 기존의 값보다 작으면 업데이트 + 우선순위 큐에 넣어준다.
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return distances


mygraph = {
    'A' : {'B':8, 'C':1, 'D':2},
    'B' : {},
    'C' : {'B':5, 'D':2},
    'D' : {'E':3, 'F':5},
    'E' : {'F':1},
    'F' : {'A':5}
}

print(dijkstra(mygraph, 'A'))