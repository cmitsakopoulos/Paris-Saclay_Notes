## Understanding dunder methods

### Representation dunder method

```Python
__repr__(variable_x)
```

You can use it as such:

```Python
def __repr__(self):
    return f"{self.barcode} and {self.meow}"
```

Python can now print the attributes of the class to which the self.attributes are assigned to, as well as giving us their location in memory.

### Set attribute

```Python
__setattr__()
```
Can help redefine the values of an attribute we already have and want to express differently. 

### Pytorch initialisation

A neural network is a set of layers which depend on each other, like PIPE in the command line. 

You would initialiase it as a normal class, but instead of "self", you enter "torch.nn.Module".

Your class attributes would be assigned as the layers which a neural network requires for processing information, going from layer one to downstream layers as required:

```Python
self.layer1 = torch.nn.Linear(data1, data2)
...
```
Another method then is required within the class, named as desired, which will designate the **order** in which you layers will work in;

```Python
def forward(self, x):
    x = self.layer1(x)
    x = self.relu(x) #intermediate analysis; bridging layer.
    x = self.layer2(x)
    return x
```
Instead of initialising the attributes as mentioned before, you can call them using the `__setattr__` method;

```Python
self.__attr__("layer1", torch.nn.Linear(data, data)) #Where you start by adding the name of the attribute, the function in the neural network, then its data
```
Within this class, "behind the scenes" a dictionary of "**parameters**" ( `parameters = {}` ) is kept which contains the values with which the *layers are interacting with or producing at any moment*.

This is ***required for a neural network to work properly***, by using `__setattr__`, you are automatically updating (***registering***) the **parameters** dictionary, by adding the name of each layer and the (mathematical) function it represents.

Now remember that a method (def) of `__setattr__` and the method of `register_parameter()` (def), can perform the same function. If both of them coexist within a class and you are manually updating the parameters dictionary, you will get double the amounts of layers.

### "Super" dunder method

To avoid problems in updating your parameters dictionary, you can use the 
```Python
class Foo():
    parameters: list
    def __init__(self):
        `super().__setattr__("parameters", [])
```
Here you have defined that parameters should be a list, and that the newly called attribute "parameters" should be accessed by all methods of the class, is **empty** when accessed by the class (for each time the class is called) and that can therefore be appended properly.

### Call dunder method

You use this dunder method in instances where you have an instance of a class which cannot be called directly like a function would; 

```Python
class MyClass:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return f"My name is {self.name}"

obj = MyClass("Chris")
print(obj())  # Now the object is callable and returns "My name is Chris"
```
### Iteration dunder method

Otherwise known as `__iter__()`, it is the equivalent of iterating within an object that can be a list or dictionary, by manual methods:

```Python
for item in object:
    pass
```
Whereas with this method:

```Python


