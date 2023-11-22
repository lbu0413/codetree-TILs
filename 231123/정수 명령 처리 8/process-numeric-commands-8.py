class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        self.node_num += 1
    

    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        
        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        
        self.node_num += 1
    

    def pop_front(self):
        if self.head == None: # 빈 리스트
            print("List is empty")
        
        elif self.head.next == None: # 노드가 하나 남은 상황
            tmp = self.head

            self.head = None
            self.tail = None
            self.node_num = 0
            return tmp.data
        
        else:
            tmp = self.head
            tmp.next.prev = None
            self.head = tmp.next
            tmp.next = None

            self.node_num -= 1
            return tmp.data
    
    def pop_back(self):
        if self.tail == None:
            print("List is empty")
        
        elif self.tail.prev == None:
            temp = self.tail
            
            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.node_num -= 1
            return temp.data
    
    
    def size(self):
        return self.node_num
    
    def empty(self):
        if self.node_num == 0:
            return 1
        else:
            return 0
    
    def front(self):
        return self.head.data
    
    def back(self):
        return self.tail.data
        

N = int(input())

dbll = DoublyLinkedList()


for i in range(N):
    input_ = input().split()
    if len(input_) == 2:
        command = input_[0]
        num = input_[1]
    
    else:
        command = input_[0]
    

    if command == 'push_front':
        dbll.push_front(num)

    if command == 'push_back':
        dbll.push_back(num)
    
    if command == 'pop_front':
        print(dbll.pop_front())
    
    if command == 'pop_back':
        print(dbll.pop_back())
    
    if command == 'size':
        print(dbll.size())
    
    if command == 'empty':
        print(dbll.empty())
    
    if command == 'front':
        print(dbll.front())
    
    if command == 'back':
        print(dbll.back())