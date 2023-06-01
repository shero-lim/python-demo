def b(a_func):
    def c():
        print("start")
        a_func()
        print("end")

    return c


@b
def a():
    print("A")


if __name__ == "__main__":
    a()
    print(a.__name__)
