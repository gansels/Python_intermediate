def create_password(func):
    def user(* args, **kwargs):
        correct = "name"
        enter_password = input("Enter password: ")
        if enter_password == correct:
            return func(* args, **kwargs)
        else:
            print("Wrong passowrd")
            return None
    return user
@create_password
def perfect_pass():
    print("The Password is correct, Open it")

perfect_pass()



