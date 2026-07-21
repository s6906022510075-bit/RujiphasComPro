import random

print('what is my magic number (1 to 100) ?')
mynumber = random.randint(1, 100)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess != mynumber:
    msg = str(ntries) + " >> "
    if ntries == 6:
        msg = "last chance >> "
    yourguess = int(input(msg))
    if yourguess < mynumber:
        print("Your guess is too low.")
    elif yourguess > mynumber:
        print("Your guess is too high.")
    ntries += 1
    
if yourguess == mynumber:
    print("Yes! it's", mynumber)
else:
    print(f'Sorry, you did not guess the magic number. The magic number was {mynumber}.')