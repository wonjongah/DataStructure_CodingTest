class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
    
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    # 맨 뒤에 노드 삽입
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            # node는 현재 마지막 노드
            # 마지막 노드의 next를 삽입할 노드로, 새로운 노드의 prev를 마지막이었던 노드로 변경
            node.next = new
            new.prev = node
            self.tail = new
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # 맨 앞부터 원하는 데이터 검색
    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node.data
            else:
                node = node.next
        return False
    
    # 맨 뒤부터 원하는 데이터 검색
    def search_from_tail(self, data):
        if self.head == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node.data
            else:
                node = node.prev
        return False

    # 특정 값을 가지고 있는 노드 앞에 원하는 값의 노드 추가
    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            # 특정 값의 node 찾기
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            # 특정 값 앞에 원하는 데이터를 가진 노드 삽입
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
    
    # 특정값 뒤에 원하는 데이터 값을 가진 노드 추가하기
    def insert_next(self, data, next_data):
        if self.head == None:
            self.head = Node(data)
            return True
        
        else:
            node = self.head
            while node.data != next_data:
                node = node.next
                if node == None:
                    return False
            next_new = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            new.next = next_new
            next_new.prev = new
            # 만약 삽입한 데이터가 마지막이라면
            if new.next == None:
                self.tail = new
            return True

double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()

print("앞에서부터 노드 3 찾기")
print(double_linked_list.search_from_head(3))

print("뒤에서부터 노드 3 찾기")
print(double_linked_list.search_from_tail(3))

print("2 앞에 1.5 삽입하기")
double_linked_list.insert_before(1.5, 2)
double_linked_list.desc()

print("1 다음에 1.3 삽입하기")
double_linked_list.insert_next(1.3, 1)
double_linked_list.desc()