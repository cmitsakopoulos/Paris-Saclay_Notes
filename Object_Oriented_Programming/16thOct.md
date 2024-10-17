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

Let’s take the example of a bank record of a person. It contains balance, transaction history, and other confidential records as part of it. Now, this bank record needs to be handled as a built-in data type to facilitate many operations. There are several methods which need access for balance and transaction history. If they directly modify the balance, they might end up inserting null values, or negative values that are very vulnerable. So, the __getitem__() and __setitem__() helps in presenting the details securely.

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
## Add info on decorators during general revision
