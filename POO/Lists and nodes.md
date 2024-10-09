## ENTER TITLE HERE

### mylist.py
```python
class Mylist:
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
        def __getitem__(self, index):
            current_node = self.head
            for i in range(index)
                current_node = current_node.next
            return current_node.data
            
if __name__ = "__main__":
    ml = Mylist()
    ml.append("A")
    ml.append("B")

```
### node.py
```python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

        def __repr__(self):
            return f"{self.data}"
```