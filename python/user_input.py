# asks for a user information and prints it out

name = input("Please input your name: ")
age = input("Please input your age: ")
location = input("Please input your location: ")
print("Welcome. Thank you for sharing your information with us")
print("Hello {}, you are {} years old and live in {}".format(
    name, age, location))
