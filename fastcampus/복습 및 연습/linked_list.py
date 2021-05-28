class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def add(data):
    node = head
    while node.next:
        node = node.next # 마지막 노드의 주소 알게 되었다
    node.next = Node(data) # 마지막 노드 주소에 새로운 노드 연결


node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

for index in range(3, 11):
    add(index)

# node1과 node2 사이에 node3 삽입
node3 = Node(1.5)
node3.next = node1.next
node1.next = node3

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)