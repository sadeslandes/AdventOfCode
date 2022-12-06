from time import perf_counter_ns

__all__ = ["Timer"]


class Timer:
    __red = "\033[91m"
    __green = "\033[92m"
    __clear = "\033[0m"

    def timer(func):
        def wrapper(*args, **kwargs):
            t1 = perf_counter_ns()
            result = func(*args, **kwargs)
            elapsed = perf_counter_ns() - t1
            color = Timer.__red if elapsed > 10 else Timer.__green
            print(f"{color}Executed in {elapsed:.4f}s{Timer.__clear}")
            return result

        return wrapper

    def __enter__(self):
        self.time = perf_counter_ns()
        return self

    def __exit__(self, type, value, traceback):
        self.time = perf_counter_ns() - self.time

    def __str__(self):
        color = Timer.__red if self.time > 10e9 else Timer.__green
        return f"{color}{self.time/1e9:.6f}s{Timer.__clear}"
