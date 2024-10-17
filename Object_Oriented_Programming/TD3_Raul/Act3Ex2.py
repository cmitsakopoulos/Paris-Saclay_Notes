import time

def exectrace(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        #print(f"Call {wrapper.calls} to {func.__name__}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

def timetrace(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        wrapper.execution_time = end_time - start_time
        return result
    wrapper.execution_time = 0
    return wrapper
    