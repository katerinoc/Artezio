"""Task 2"""
from time import sleep, time


def time_counter(f):
    def wrapper(*args, **kwargs):

        start = time()
        res = f(*args, **kwargs)
        print("working time:" + str(time()-start))
        return res
    return wrapper


def time_methods(*class_methods):

    def decorator(class_instance):
        def wrapper(*args, **kwargs):
            for item in class_methods:
                if hasattr(class_instance, item):
                    setattr(class_instance, item, time_counter(getattr(class_instance, item)))
            return class_instance(*args, **kwargs)
        return wrapper
    return decorator


@time_methods('inspect', 'finalize')
class Spam:
    def __init__(self, s):
        self.s = s

    def inspect(self):
        sleep(self.s)

    def foo(self):
        return self.s


a = Spam(2)
a.inspect()
a.foo()
