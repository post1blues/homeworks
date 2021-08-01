
name = input("Enter your name: ").strip()
age = input("Enter your age (only numbers): ").strip()

if not name or not age or not age.isnumeric():
    print("Your name or your age is incorrect")
else:
    print("Hello, {}, on your next birthday you'll be {} years.".format(name, int(age) + 1))