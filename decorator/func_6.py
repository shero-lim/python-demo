from functools import wraps


# 返回包裹函数的函数
def logit(logfile="out.log"):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            with open(logfile, "a") as opened_file:
                opened_file.write(log_string + "\n")
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@logit()
def myfunc1():
    pass


myfunc1()


# output: myfunc1 was called
# 现在一个叫做out.log的文件出现了，里面的内容就是上面的字符串

@logit(logfile="func2.log")
def myfunc2():
    pass


myfunc2()
# output: myfunc2 was called
# 现在一个叫做func2.log的文件出现了，里面的内容就是上面的字符串


