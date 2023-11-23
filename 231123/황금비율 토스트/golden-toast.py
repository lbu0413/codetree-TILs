class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.head = self.END
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None
    
    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)
        
        else:
            new_node = Node(new_data)
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node
        
    
    def erase(self, node):
        next_node = node.next

        if node == self.begin():           # 만약 head가 삭제되어야 한다면
            temp = self.head          
            temp.next.prev = None          # 새로 head가 될 노드의 prev값을 지워줍니다.
            self.head = temp.next          # head값을 새로 갱신해주고
            temp.next = None               # 이전 head의 next 값을 지워줍니다.

        else:                              # head가 삭제되는 것이 아니라면
            node.prev.next = node.next     # 바로 전 노드의 next값을 바꿔주고
            node.next.prev = node.prev     # 바로 다음 노드의 prev값을 바꿔주고
            node.prev = None               # 해당 노드의 prev 와 
            node.next = None               # 해당 노드의 next 값을 모두 지워줍니다.

        return next_node
    
    def insert(self, node, new_data):
        if node == self.end():             # node가 맨 끝 위치에 있다면
            self.push_back(new_data)       # 맨 뒤에 원소를 추가합니다.   

        elif node == self.begin():         # node가 맨 앞 위치에 있다면
            self.push_front(new_data)      # 맨 앞에 원소를 추가합니다.

        else:                              # 그렇지 않다면
            new_node = Node(new_data)      # 새로운 노드를 만들어줍니다.
            new_node.prev = node.prev      # 새로운 노드의 prev값을 node의 prev값으로 하고
            new_node.next = node           # 새로운 노드의 next값을 node로 하고
            node.prev.next = new_node      # node의 prev의 next값을 새로운 노드로 변경하고
            node.prev = new_node           # node의 prev 값을 새로운 노드로 변경합니다.

    def begin(self):
        return self.head
    
    def end(self):
        return self.tai

dbll = DoublyLinkedList()
N, M = map(int, input().split())
status = input()
for s in status:
    dbll.push_back(s)

print(dbll)
for i in range(M):
    recipe = input().split()
    if len(recipe) == 1:
        code = recipe[0]
    else:
        code = recipe[0]
        letter = recipe[1]
    
    if code == 'L':