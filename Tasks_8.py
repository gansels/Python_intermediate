def deco(func):
    def new_func():
        print(f" The new function ")
        func()
        print(f" The new function when i am calling ")
    return new_func

@deco
def trying_decorator():
    print("Hello decorator")


trying_decorator()


