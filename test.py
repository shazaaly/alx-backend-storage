
call_count = {}

def count_calls(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        call_count[method.__name__] = call_count.get(method.__name__, 0) + 1
        print(f"Call count of {method.__name__}: {call_count[method.__name__]}")
        return method(*args, **kwargs)
    return wrapper

@count_calls
def some_function():
    print("Function is running")

some_function()  # This will increment the count and print it
