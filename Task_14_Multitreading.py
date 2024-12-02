# tasks_14

import threading


class ThreadWithReturnValue(threading.Thread):
    def __init__(self, target, args=()):
        super().__init__()
        self.target = target
        self.args = args
        self._return = None

    def run(self):
        self._return = self.target(*self.args)

    def join(self):
        super().join()
        return self._return

# now write the func to calculate the sum
def caln_sum():
    return sum(range(1, 1000000))


# now write the func for multiply

def multiply():
    result = 1
    for i in range(1, 100):
        result *= i
    return result


# threading
thread_sum = ThreadWithReturnValue(caln_sum)
thread_multi = ThreadWithReturnValue(multiply)

# starting the thread
thread_sum.start()
thread_multi.start()

# Now for the result
result_sum = thread_sum.join()
result_1_multiply = thread_multi.join()

# Print the result
print(f"Sum of the calculation is:", result_sum)

print(f"Multiplication of the value is:", result_1_multiply)

