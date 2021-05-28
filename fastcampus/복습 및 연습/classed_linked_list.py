class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data): # 맨끝에 추가
        if self.head == '': # 헤드 없다면 노드 새로 생성해서 헤드로
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data) # 맨마지막 노드의 주소에 새로운 노드 연결 및 생성
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(1,11):
    linkedlist1.add(data)
linkedlist1.desc()