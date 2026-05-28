
import random
import string

pass_len = int(input("Enter the password length you need : "))
pass_values = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(pass_values)

print("Your Password is .... (",password,")")
