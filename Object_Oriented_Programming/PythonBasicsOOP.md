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
