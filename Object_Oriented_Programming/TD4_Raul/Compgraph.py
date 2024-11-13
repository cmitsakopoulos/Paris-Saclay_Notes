
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
class Node:
    id = 0

    def __init__(self, data):
        self.id = Node.id
        Node.id += 1

        self.data = data
        self.successors = []
        self.predecessors = []
    
    def add_successor(self, successor):
        self.successors.append(successor)

    def get_successors(self):
        return self.successors

    def add_predecessor(self, predecessor):
        self.predecessors.append(predecessor)

    def get_predecessors(self):
        return self.predecessors

    def __repr__(self):
        return f'data {self.data}\n'

    def to_nx_graph(self, nx_graph=None):
      if nx_graph is None:
        nx_graph = nx.DiGraph()  # Create a new graph if none is provided
      nx_graph.add_node(self.id, label=None)
      return nx_graph
    

class MyGraph:
    def __init__(self) -> None:
        self.nodes = {}

    def add_node(self, data):
        node = Node(data)
        self.nodes[node.id] = node
        return node

    def add_edge(self, source, destination):
        source.add_successor(destination)
        destination.add_predecessor(source)

    def topological_order(self, start):
        """
        returns the list of nodes in a topological order
        so that the operations will be executed starting from
        the inputs until the last node of the graph.
        """
        seen = set()
        path = []
        q = [start]
        while q:
            v = q.pop()
            if v not in seen:
                seen.add(v)
                path.append(v)
            q.extend(v.get_predecessors())

        return path

    def map(self, a_function):
        for node in self.nodes.values():
            a_function(node)

    def copy(self, a_graph):
        pass

    def __iter__(self):
        pass

    def __eq__(self, a_graph):
        pass

    def __repr__(self):
        pass

class ComputationGraph:
    my_graph = MyGraph()
    def __init__(self, fun):
        print("init")
        self.fun = fun
    
    def __call__(self, *args, **kwargs):
        print("call")
        res = self.fun(*args, **kwargs)
        res_node = self.my_graph.add_node(res)
        fun_node = self.my_graph.add_node((self.fun, args, None))
        self.my_graph.add_edge(fun_node, res_node)
        return res
    
@ComputationGraph
def rand(*args):
    return np.random.rand(*args)

@ComputationGraph
def multiply(a,b):
    print("multiply performed") # Print to check if computation is performed
    return np.multiply(a,b)

a = rand(2,3)
b = rand(2,3)
c = rand(2,3)

multiply(multiply(a,b), multiply(b,c))

# Create a new directed graph
nx_graph = nx.DiGraph()

# Add all nodes and edges to the nx_graph
for node in ComputationGraph.my_graph.nodes.values():
    nx_graph.add_node(node.id, label=str(node.data))
    for successor in node.get_successors():
        nx_graph.add_edge(node.id, successor.id)
pos = nx.spring_layout(nx_graph)
nx.draw(
    nx_graph, pos, with_labels=False, arrows= 1,
    node_size=1500, node_color="skyblue", font_size=10, font_weight='bold')
plt.show()

# Get the graph after computation
result = c
print(result)