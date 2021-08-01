
phone_number = input("Enter your phone number (only numerical characters): ")

if not phone_number.isnumeric():
    print("Phone number should contain only numerical characters")
elif len(phone_number) != 10:
    print("Phone number should be only 10 characters long")
else:
    print("Phone number is correct")