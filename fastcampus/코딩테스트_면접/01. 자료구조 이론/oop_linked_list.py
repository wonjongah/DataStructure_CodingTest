class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    # 맨 앞의 노드까지 생성
    def __init__(self, data):
        self.head = Node(data)

    # 맨 뒤에 추가
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            # 맨 마지막 노드에 노드 생성해서 연결
            node.next = Node(data)

    # 노드 순회 + 출력
    # 첫 노드를 넘겨줘서 그곳부터 순회
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    # 노드 삭제
    def delete(self, data):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        # 첫 번째 노드 삭제
        if self.head.data == data:
            temp = self.head # 객체 삭제 위해 임시 변수에 저장
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                # 노드의 주소가 가리키는 데이터 값이 삭제하려는 노드라면
                if node.next.data == data:
                    temp = node.next
                    # 이전의 노드의 주소값을 삭제하려는 노드가 가리키는 주소로 변경
                    node.next = node.next.next
                    del temp
                    return
                # 노드의 주소가 가리키는 데이터 값이 아니라면, 다음 노드로 이동
                else:
                    node = node.next
                    
    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node.data
            else:
                node = node.next
            
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

# head 존재
print(linkedlist1.head)

linkedlist1.delete(0)
# head 삭제 -> None
print(linkedlist1.head)

linkedlist1 = NodeMgmt(0)

for data in range(1, 10):
    linkedlist1.add(data)

linkedlist1.desc()
print("노드 4 삭제")
linkedlist1.delete(4)
linkedlist1.desc()
print("노드 9 삭제")
linkedlist1.delete(9)
linkedlist1.desc()
print("노드 3 찾기")
print(linkedlist1.search_node(3))