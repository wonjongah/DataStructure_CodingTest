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

    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next # 마지막 노드도 가능
                    del temp
                    return
                else:
                    node = node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(1,11):
    linkedlist1.add(data)
linkedlist1.desc()

print("3 삭제")

linkedlist1.delete(3)
linkedlist1.desc()

print("0 삭제")

linkedlist1.delete(0)
linkedlist1.desc()

print("10 삭제")

linkedlist1.delete(10)
linkedlist1.desc()