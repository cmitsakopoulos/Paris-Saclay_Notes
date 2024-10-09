from node import Node

class MyList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return


if __name__=='__main__':
    ml = MyList()
    ml.append("A")