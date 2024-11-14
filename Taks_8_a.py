def create_password(password):
    def decor(func):
        def user():
            user_password = input("Enter password: ")
            if user_password == password:
                return func()
            else:
                print("Wrong passowrd")
        return user
    return decor
@create_password("name1213")
def perfect_pass():
    print("The Password is correct, Open it")

perfect_pass()


