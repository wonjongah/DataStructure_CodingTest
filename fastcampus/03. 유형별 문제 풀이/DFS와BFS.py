from collections import deque

def dfs(v):
    print(v, end=" ")
    # 방문한 원소는 방문 True
    visited[v] = True
    for e in adj[v]:
        # 방문 안 했으면 dfs 재귀적 호출
        if not(visited[e]):
            dfs(e)

def bfs(v):
    q = deque([v])
    # 큐가 빌 때까지 반복
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=" ")
            for e in adj[v]:
                # 방문하지 않았다면 큐에 넣어줌
                if not visited[e]:
                    q.append(e)

n, m, v = map(int, input().split())
# n + 1개의 빈 리스트
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    # 각각 서로의 연결 리스트에 추가
    adj[x].append(y)
    adj[y].append(x)

# 각각의 정점에 연결된 정점들을 정렬
# ****가장 낮은 곳부터 방문하도록
for e in adj:
    e.sort()

# 방문하지 않은 것으로 초기화
visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)