def dfs(graph, start_node):
    need_visit = list()
    visited = list()
    # need_visit, visited = list(), list()
    # 한 줄로 표현 가능
    
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            # need_visit.extend(graph[node][::-1])
            need_visit.extend(graph[node]) 
            # 회문을 넣든 상관 없다, 어딜 먼저 순회하냐의 차이
    return visited

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(dfs(graph, 'A'))