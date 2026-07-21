score = int(input('Enter a test score: '))

while score < 0 or score > 100:
    print('Error: The score cannot be neggative')
    print('or greater than 100.')
    score = int(input('Enter a correct score: '))