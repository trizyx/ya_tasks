love_string = input()
number = int(input())

with open('fortune.txt', 'w') as output:
    if love_string == 'любит':
        out = 'любит' if number % 2 == 1 else 'не любит'
    else:
        out = 'не любит' if number % 2 == 1 else 'любит'
    
    print(out, file=output)
