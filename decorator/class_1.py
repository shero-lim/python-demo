from functools import wraps


class logit(object):
    def __init__(self, logfile="out2.log"):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + "was called"
            print(log_string)
            with open(self.logfile, "a") as opened_file:
                opened_file.write(log_string + "\n")
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        #logit只打日志，不做别的
        pass


@logit()
def myfunc1():
    pass


myfunc1()


class email_logit(logit):
    def __init__(self, email="admin@myproject.com", *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        print("发送一封邮件" + self.email)


@email_logit()
def myfunc2():
    pass


myfunc2()

# @email_logit 将会和 @logit产生同样的效果，但是在打日志的基础上，还会多发送一封邮件给管理员
