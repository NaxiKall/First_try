import random
import string

chars = int(input("Length of password: "))

password = "".join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(chars)])

print("Your password: " + password)


