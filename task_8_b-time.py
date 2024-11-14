#import time
# start = time.time()
# time.sleep(1)
# end = time.time()
# print(f"Uplynulý čas {end - start:.4f}")
import time
#decorator to create time and function using import time
def func_time(function):
    def control(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Uplynulý čas {end - start:.4f} sec")
        return result
    return control
#creating decorator
@func_time
def create_func_time():
    print(f" time function is good: ")
    time.sleep(1)
# Call the function
create_func_time()


