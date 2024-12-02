def exectrace(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls} to {func.__name__}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

# Example usage:
@exectrace
def example_function():
    print("Function is called")

example_function()
example_function()
example_function()