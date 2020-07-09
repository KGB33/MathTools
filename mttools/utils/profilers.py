"""
Tools used for profiling tests for efficiency
"""
from statistics import mean
from typing import Literal, Callable
from time import perf_counter_ns


class Timer:
    """
    A Decorater to mesure the runtime of a function.
    """

    def __init__(
        self,
        unit: Literal["ns", "us", "ms", "s", "min"] = "ms",
        message: str = None,
        trials: int = 1,
    ):
        """
        Decorator that times the function runtime, then prints the result
        
        unit (optional): Unit that the time is displayed in, default is ms
        
        message (optional): Message that is printed with the elapsed time
        """
        self.unit = unit
        self.message = message
        self.num_trials = trials

    def __call__(self, func: Callable):
        """
        func: The function to be timed
        """

        def wrapper_timer(*args, **kwargs):
            times = []
            for _ in range(self.num_trials):
                before = perf_counter_ns()
                return_value = func(*args, **kwargs)
                after = perf_counter_ns()
                times.append(after - before)
            av_time = mean(times)
            conversion = self.convert_time()
            time = "{:.3f}".format(av_time / conversion)
            print("\n\nTime Elapsed: {0}{1}".format(time, self.unit))
            if self.message is not None:
                print("\t{}".format(self.message))
            return return_value

        return wrapper_timer

    def convert_time(self) -> int:
        """
        returns the correct conversion
        factor for the given unit
        """
        if self.unit == "ns":
            conversion = pow(10, 0)
        elif self.unit == "us":
            conversion = pow(10, 3)
        elif self.unit == "ms":
            conversion = pow(10, 6)
        elif self.unit == "s":
            conversion = pow(10, 9)
        elif self.unit == "min":
            conversion = 6 * pow(10, 10)
        else:
            print(
                "\n\nBad unit given to @timer, Valid units are:"
                "\n\tns, us, ms, s, min"
                "\n\tUsing default ms"
            )
            conversion = pow(10, 6)
            self.unit = "ms"
        return conversion
