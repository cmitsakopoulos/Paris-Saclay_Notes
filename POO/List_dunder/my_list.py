from node import Node

class MyList:
    def __init__(self):
        self.head = None
    
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
    
    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next


if __name__=='__main__':
    ml = MyList()
    ml.append("A")