print("this is the beginning of a python repository")
name = "linford-web "
age = 23
email = "linfordobara@gmail.com "


def detail():
    height = 5.6
    print("my height is", height) # this prints out the in-function, this is the variable called in the function.

    global name, age, email
    print("These are my details:", name, age, email, height)

detail()
