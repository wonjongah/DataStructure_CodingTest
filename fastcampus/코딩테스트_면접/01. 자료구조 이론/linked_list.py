# 노드 클래스
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next: # node.next가 None이 아니라면, 마지막 노드를 찾기 위해
        node = node.next
    node.next = Node(data)

# 노드 생성 및 노드 추가
node = Node(1)
head = node
for index in range(2, 10):
    add(index)

# 전체 노드 출력
while node.next:
    print(node.data)
    node = node.next
print(node.data)

# 노드 삽입
node = head
node3 = Node(1.5)
search = True
while search:
    if node.data == 1: # 삽입할 위치 앞의 노드 찾기
        search = False
    else:
        node = node.next
node_next = node.next # 전의 노드가 가리키고 있는 곳 임시 저장
node.next = node3 # 전의 노드 주소를 삽입할 노드로 변경
node3.next = node_next # 삽입한 노드가 가리키는 곳을 전의 노드가 기리키고 있는 곳으로 저장

print()
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)