from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        elapsed = time() - t1
        red = "\033[91m"
        green = "\033[92m"
        clear = "\033[0m"
        color = red if elapsed > 10 else green
        print(f"{color}Executed in {elapsed:.4f}s{clear}")
        return result

    return wrapper
