# Generates a random password of user-identified length.
# Password must contain at least one upper-case letter, one
#     lower-case letter, one number, and one special character.


from random import randint

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
specials = "!@#$%^&*?~_+-=."
options = letters+numbers+specials

length = 0
while length < 16:
    temp = input("How long of a password do you want?  Use an integer >= 16.")
    # catch entry of a character
    try:
        tempFloat = float(temp)
    except ValueError:
        continue
    # catch entry of a float (except for n.0, which is allowed)
    if int(tempFloat) != tempFloat:
        length = 0
        continue
    else:
        length = int(tempFloat)

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

print(result)
