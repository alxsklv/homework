running = True

while running:
    A = int(input('Enter even number: '))
    if A%2 == 0:
        print('Digit is even\n')
    else:
        print('False! Digit is odd\n')
        break