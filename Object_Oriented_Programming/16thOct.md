## Understanding dunder methods

### Representation dunder method and string:

Using the `repr`on its own, **not as a function** (no def) would yield a response along the lines of:

```Python
<__main__.Ocean object at 0x102892860>
<__main__.Ocean object at 0x102892860>
```
Where ***Ocean (a class) is the object*** in question (inserted in the `__repr__` brackets) and the following barcode represents the ***memory address*** of the object in your computer.

In order to use it as a dunder method:

```Python
__repr__(variable_x)
```

You can use it as such:

```Python
#Class is Miauler, with one parameter; a boolean assigned to meow.
def __repr__(self):
    return f"Meow = {self.meow}"

call = Miauler(True)
print(repr(call))

Output:
Meow = True
```
Now the `__str__` method is very similar to repr, but behaves closer to print than `__repr__`

### Set attribute

**Python `__setattr__()`**:

The `__setattr__()` method can redefine the values of an existing attribute within an object. This can be particularly useful for ensuring that the values assigned to attributes meet certain criteria or for modifying their values before they are set.
 
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

Otherwise known as `__iter__()`, it is the equivalent of iterating within an object that can be a list or dictionary, by manual methods; a **replacement for a "for" loop**:
```Python
for item in object:
    pass
```
Whereas using this method, you could for example apply the following:

```Python
    def __iter__(self):
        node = self.head
        while node is not None: #Check that the object you are iterating is not empty, or it will fail.
            yield node #return the value it has iterated through
            node = node.next #continue iterating
        return self
``` 
### Get item method

Imagine a class which models a building. Within the data for the building it includes a number of attributes, including descriptions of the companies that occupy each floor:

Without using `__getitem__` we would have a class like this:
```Python
class Building(object):
     def __init__(self, floors):
         self._floors = [None]*floors
     def occupy(self, floor_number, data):
          self._floors[floor_number] = data
     def get_floor_data(self, floor_number):
          return self._floors[floor_number]

building1 = Building(4) # Construct a building with 4 floors
building1.occupy(0, 'Reception')
building1.occupy(1, 'ABC Corp')
building1.occupy(2, 'DEF Inc')
print( building1.get_floor_data(2) )
```
We could however use `__getitem__` (and its counterpart `__setitem__`) to make the usage of the Building class 'nicer':
```Python
class Building(object):
     def __init__(self, floors):
         self._floors = [None]*floors
     def __setitem__(self, floor_number, data):
          self._floors[floor_number] = data
     def __getitem__(self, floor_number):
          return self._floors[floor_number]

building1 = Building(4) # Construct a building with 4 floors
building1[0] = 'Reception'
building1[1] = 'ABC Corp'
building1[2] = 'DEF Inc'
print( building1[2] )
```
Whether you use `__setitem__` like this really depends on how you plan to abstract your data - in this case we have decided to treat a building as a container of floors (and you could also implement an iterator for the Building, and maybe even the ability to slice - i.e. get more than one floor's data at a time - it depends on what you need.

## Manipulating class attributes

You can reassign a class attribute (an attribute initiated under the `def __init__`) by doing the following:
```Python
class Example:
    an_attribute = "coq" #Yes you can actually do this in a class

example = Example()
example.attr = "not coq" #Can update an attribute's value using this method
print(example)

Output:
"not coq"
```
## Add info on decorators during general revision
