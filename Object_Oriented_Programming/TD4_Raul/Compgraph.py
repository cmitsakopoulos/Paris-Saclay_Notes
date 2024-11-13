
import numpy as np

class ComputationGraph:
    def __init__(self, func):
        self.graph = {}
        self.values = {}
        self.order = []
        self.grads = {}
    
    @staticmethod
    def __new__(cls, *args, **kwargs):
        obj = super(ComputationGraph, cls).__new__(cls)
        obj.__init__(*args, **kwargs)
        return obj
    

    
    
    def __call__(self, *args, **kwargs):
        res = self.forward(*args, **kwargs)
        return res

    def add(self, node, inputs, value):
        self.graph[node] = inputs
        self.values[node] = value
        self.order.append(node)

    @property
    def forward(self):
        for node in self.order:
            inputs = [self.values[n] for n in self.graph[node]]
            self.values[node] = node.forward(inputs)

    def backward(self):
        self.grads = {node: np.zeros_like(self.values[node]) for node in self.order}
        self.grads[self.order[-1]] = np.ones_like(self.values[self.order[-1]])
        for node in reversed(self.order):
            inputs = [self.values[n] for n in self.graph[node]]
            grads = [self.grads[n] for n in self.graph[node]]
            self.grads[node] = node.backward(inputs, self.grads[node])
            for i, n in enumerate(self.graph[node]):
                self.grads[n] += grads[i]

    def zero_grad(self):
        self.grads = {node: np.zeros_like(self.values[node]) for node in self.order}

    def step(self, lr):
        for node in self.order:
            self.values[node] -= lr * self.grads[node]

    def __getitem__(self, node):
        return self.values[node]

    def __setitem__(self, node, value):
        self.values[node] = value

    def __repr__(self):
        return str({node: self.values[node] for node in self.order})

    def __str__(self):
        return str({node: self.values[node] for node in self.order})
    
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