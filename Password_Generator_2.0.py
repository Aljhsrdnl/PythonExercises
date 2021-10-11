import string
import random
ans = "y"
while ans == "y":
    ans = str(input("would you like to generate a password? (y/n): "))
    if ans == "y":
        choices = string.ascii_letters + string.punctuation + string.digits
        passLen = int(input("How long do you like your password to be?: "))

        li = random.choices(choices, k=passLen)
        h = ""
        password = h.join(li)
        print("Your password is: " + password)
    else:
        break
    
