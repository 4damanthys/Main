def login(login, password):
    if login == "user" and password == "teste1234":
        print(f"Welcome, {login}!")
    else:
        print(f"Oh no!")

user = input("USERNAME >>>>>>> ")
pswrd = input("PASSWORD >>>>>>> ")

login(user, pswrd)