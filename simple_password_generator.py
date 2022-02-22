# DomirScire
# Early python projects
import random
import string

print("Weak:    0\nStrong:  1\nInsane:  2\n")

preSet=input("Choice: ")
preSet=int(preSet)


if preSet == 0:
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for x in range(12))
    print(password)
elif preSet == 1:
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for x in range(16))
    print(password)
elif preSet == 2:
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for x in range(32))
    print(password)

# Secret Option
elif preSet == 6:
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for x in range(128))
    print(password)
else:
    print("WRONG Input")
