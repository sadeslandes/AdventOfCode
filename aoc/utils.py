from time import perf_counter

__all__ = ["Timer"]


class Timer:
    __red = "\033[91m"
    __green = "\033[92m"
    __clear = "\033[0m"

    def timer(func):
        def wrapper(*args, **kwargs):
            t1 = perf_counter()
            result = func(*args, **kwargs)
            elapsed = perf_counter() - t1
            color = Timer.__red if elapsed > 10 else Timer.__green
            print(f"{color}Executed in {elapsed:.4f}s{Timer.__clear}")
            return result

        return wrapper

    def __enter__(self):
        self.time = perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.time = perf_counter() - self.time

    def __str__(self):
        color = Timer.__red if self.time > 10 else Timer.__green
        return f"{color}{self.time:.4f}s{Timer.__clear}"
