def bfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit: # 전부 순회하는 동안
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node]) # 그 뒤에 해당 키의 밸류 붙여넣기, +와 같다.
    
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

print(bfs(graph, 'A'))