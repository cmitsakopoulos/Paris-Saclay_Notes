# Basics

# Notes Basics

Tuples are immutable, they are the shit I was using to return multiple variables from functions. Ex: genstart, genend, etc. Just use lists or dictionaries.  

Methodologies for modelling can vary depending on the need; obviously, if you are creating **planes** etc, you need accurate and robust systems.  
**Code reusability** is paramount.  

**Non-structured programming** (*imperative programming*): Functions that do stuff, without a given structure or consecutive functions.  
**1st order programming**: ex. interactions between different functions, with limited dependencies, clean code which is less prone to error.  
**Higher order programming**: when you consider functions as a variable, or in other words, when you concatenate functions, integrate them with each other.  
**Declarative programming**: when you work towards a certain goal, SQL, where the process is not defined, as in imperative programming, you express the logic but not the control flow; think of **PROLOG**, where you program a certain logical framework, to handle data or assign data.

# Understanding dunder methods

## Representation dunder method and string

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

For example:

```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of Person
p = Person("Alice", 30)

# Using setattr to change the age attribute, without permanently modifying the initial instance of the object.
setattr(p, 'age', 31)

# Using getattr to verify the change
print(getattr(p, 'age'))  # Output: 31
```

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

Now remember that a method (def) of `__setattr__` and the method of `register_parameter()` (def), can perform the same function. If both of them coexist within a class and you are manually updating the parameters dictionary, you will get double the amount of layers.

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

Additionally, you can use `__call__` to call the decorator without getting the results provided by the decorated function.

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

Let’s take the example of a bank record of a person. It contains balance, transaction history, and other confidential records as part of it. Now, this bank record needs to be handled as a built-in data type to facilitate many operations. There are several methods which need access for balance and transaction history. If they directly modify the balance, they might end up inserting null values, or negative values that are very vulnerable. So, the **getitem**() and **setitem**() helps in presenting the details securely.

```Python
class bank_record: 
 
 def __init__(self, name): 
  
  self.record = { 
      "name": name, 
      "balance": 100, 
      "transaction":[100] 
      } 

 def __getitem__(self, key): 
  
  return self.record[key] 

 def __setitem__(self, key, newvalue): 
  
  if key =="balance" and newvalue != None and newvalue>= 100: 
   self.record[key] += newvalue 
   
  elif key =="transaction" and newvalue != None: 
   self.record[key].append(newvalue) 
 
 def getBalance(self): 
  return self.__getitem__("balance") 

 def updateBalance(self, new_balance): 
  
  self.__setitem__("balance", new_balance) 
  self.__setitem__("transaction", new_balance)  
 
 def getTransactions(self): 
  return self.__getitem__("transaction") 

 def numTransactions(self): 
  return len(self.record["transaction"]) 

sam = bank_record("Sam") 
print("The balance is : "+str(sam.getBalance())) 

sam.updateBalance(200) 
print("The new balance is : "+str(sam.getBalance())) 
print("The no. of transactions are: "+str(sam.numTransactions())) 

sam.updateBalance(300) 
print("The new balance is : "+str(sam.getBalance())) 
print("The no. of transactions are: "+str(sam.numTransactions())) 
print("The transaction history is: "+ str(sam.getTransactions())) 
```

If the attributes of a class are to remain private (only accesible by that class), then the getitem method allows you to access the information of that attribute (which should be stored in for ex. a list or dictionary), without **needing to store them in new variables, can check for states and can handle data manipulation of the attribute when paired with setitem**.

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

## Object Diagram to convert into Python

![alt text](ObjectDiagramTD.png)

## Classes in Python

Introduce class: 

`class name_here:`  

Under class, indent and initialise: 

```python
def __init__(self, attribute, attribute):
```

**self** allows Python to access within the boundaries of the class.  

Having initialised the class, follow up by **indenting** and introducing class **attributes**, for instance:

`self.title = title`
`self.author = author`
`self.isbn = isbn`

These attributes and their assigned values are **only** accessible within the same instance; so within the confines of `def _init_`.
Also, the above example assigns the attributes to the information that will be obtained by `def _init_(self, title, author)`; 

Whereas, you could add:
```python
class Chat:
Cleio = "MeowCat"
def _init_(self, meow)
    self.Cleio = meow
```
For any code **outside** of the instance `def _init_`, _Cleio is equal to a MeowCat_, however **within** the instance, _Cleio is equal to whichever value **meow** obtains_; if **meow** obtains no value, Cleio remains a MeowCat.

Variables which are assigned to the **instance** curator **self**, are called **private variables**. 

Title is obtained by a **method** which does its calculations then returns the title:

```python
def get_title(self):
    do_something
    return self.title
```
In this example, the **method/function** get_title can return "Miauler". "Miauler" will then be assigned to `self.title`

## Good practice in Python OOP

While it is feasible to have all necessary classes within the same Python file, it is often preferred to split your **packages**(=Classes, their attributes and methods) into **inteconnected Python files**.

Given that the classes are in their own distinct Python files and within the same directory, you can import a class as such:

Class 1 = woof = Dog.py

Initialising parameters of woof:
```python
def _init_(self, treats):
```
main file = main.py
```python
#Within main.py;
from Dog import woof
```
In this case we have imported class woof from the Dog.py file. Then, one could:

```python
my_dog = woof('chocolate')
print(my_car.display_info())
```
Here, using the methods within woof class, the dog will die as it eats the chocolate; printing a corresponding message.

