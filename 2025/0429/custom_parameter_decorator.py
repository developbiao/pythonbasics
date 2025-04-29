# -*- encoding: utf-8 -*-

# Custom parameter Decorator
# This is a decorator factory that accepts parameters.

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


# Usage example
@repeat(times=3)
def greet(saying):
    print(f"Hello, {saying}!")

greet("日进斗金!")

