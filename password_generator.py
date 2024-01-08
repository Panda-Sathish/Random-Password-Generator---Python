import random

print("Welome to Random Password Generator")

randomChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqurstuvwxyz1234567890~!@#$%^&*?"

num_len = int(input("Enter the Number Of Passwords You Need : "))

pass_len = int(input("Enter the Length of Password : "))


print("Here is your Random Password")

for x in range(num_len):
    pas = " \n"

    for y in range(pass_len):
        pas = pas + random.choice(randomChars)

    print(pas)
 
