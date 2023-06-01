from functools import wraps


def b(f):
    @wraps(f)
    def decorated():
        if not can_run:
            return "Function will not run"
        return f()

    return decorated


@b
def a():
    return ("Function is running")


can_run = True
print(a())

can_run = False
print(a())
