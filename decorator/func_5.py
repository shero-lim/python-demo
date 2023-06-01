from functools import wraps


def logit(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    return x + x

result = addition_func(4)
print(result)