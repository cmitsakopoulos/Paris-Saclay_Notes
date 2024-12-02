# Decorators & Methods

## @staticmethod

```Python
class CustomStaticMethod(object):
    def __init__(self, callable):
        self.f = callable
    def __get__(self, obj, type = None):
        print(f"call to __get:: with obj={obj} type = {type}")
        return self.f


```

## @classmethod

huh

## Project: A min neural network with PyTorch

Creating the ULM library
Elements that we set to implent
Tensor, layer, parameters, Mode (learnatol), Optimizer, NeuralNetwork, Linear 
Loss 