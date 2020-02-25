"""Task 1"""

from time import sleep, time


def average_time(N=2):
    def decorator(function):
        count = []

        def wrapper(*args, **kwargs):
            current_time = time()
            result = function(*args, **kwargs)
            R = time()-current_time
            count.append(R)
            all_time = 0
            for item in count:
                all_time = all_time + item

            print("function runs:" + str(all_time/len(count)))
            print(result)
            return all_time/len(count)

        return wrapper
    return decorator


@average_time(N=2)
def foo(a):
    sleep(a)
    return a


foo(3)
foo(7)
foo(1)
