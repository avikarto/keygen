# Generates a random password of user-identified length.
# Password must contain at least one upper-case letter, one
#     lower-case letter, one number, and one special character.


from random import randint

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
specials = "!@#$%^&*?~_+-="
options = letters+numbers+specials

length = int(input("How long of a password do you want? "))

while True:
    pw = []
    for i in range(length):
        if randint(1, 2) == 1:
            pw.append(options[randint(0, len(options)-1)])
        else:
            pw.append(options[randint(0, len(options)-1)].upper())
    # password must have at least one number and one special character
    if [x for x in pw if x in numbers] != [] and [x for x in pw if x in specials] != []:
        # password must have at least one upper and one lower case letter
        result = "".join(pw)
        if result != result.lower() and result != result.upper():
            break
# while

print(result)
