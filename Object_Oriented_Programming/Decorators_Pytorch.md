# LOTS to fill in from lost lecture

## @property

- Where one would call the class Property through `Property(x)', using a decorator on a function you can do the following:

```Python
@property
def x(self):
    return self.__x
```
"" are empty to depict the placeholder for a new term

In other words, the property class will be called, **fget** will be altered state from **None** *to the* ***value of x***.

## @x.setter

```Python
@x.setter
def x(self, value):
    self.__x = value
```
