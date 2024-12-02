# Decorators and Pytorch (06/11/2024)

## Lambda Function

Let's step back a little and define what's a lambda fucntion. It's a function written inside a variable or object like this one:

```Python
result = calculate(
 lambda x, y: x+y,
 4,
 6
)

```

This is a basic sum function it works exactly as this function:

```Python
def add(x,y):
 return x+y

result = add(4,6)

```

Except this function actually takes space inside the memory while the lamda function is resolved inside of the variable and deleted, returning only the final value, saving memory.

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

## Look up custom decorators
