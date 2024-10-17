import time
import matplotlib.pyplot as plt

def exectrace(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls} to {func.__name__}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

def timetrace(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        wrapper.execution_time = end_time - start_time
        print(f"Execution time: {wrapper.execution_time}")
        return result
    wrapper.execution_time = 0
    return wrapper

@exectrace
@timetrace
def myfunc(n):
    x = (1000**n)/n -1
    return x

list_x = []
list_y = []

for i in range(2, 10):
    y = myfunc(i)
    list_x.append(i)
    list_y.append(y)
    print(f"Result: {y}")

plt.plot(list_x, list_y)

    