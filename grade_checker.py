try:
    score = ''
    i = 0
    while i < 40:
        print('*' * i)
        i += 1
    print('''
            Grade Checker   
        ''')
    print('''           Type 1000 to quit 
    ''')
    while score != 'quit':
        score = float(input('Enter Your Score: '))
        if score == 1000:
            print('Grade Checker quitted')
            break
        elif score > 100:
            print('input a score from range 0 - 100')
        elif score >= 70 <= 100:
            print('A')
        elif score >= 59 < 70:
            print('B')
        elif score >= 40 < 59:
            print('C')
        elif score >= 30 < 40:
            print('D')
        elif score >= 20 < 30:
            print('E')
        elif score >= 0 < 20:
            print('F, You Failed')

except:
    print('invalid input, Try again')