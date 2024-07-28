import random
import string
charValues = string.ascii_letters + string.digits + string.punctuation
while True:
    try:
        pass_len = int(input("Enter the required length of the password: "))
        if pass_len < 8 :
            print("Password length must be at least 8 characters .")
        elif pass_len >=15:
            print("Password must be of maximum 15 caharacters")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
password = "".join([random.choice(charValues)for i in range(pass_len)])
print("YOUR PASSWORD IS:", password)       