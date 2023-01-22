try:
    number=int(input('enter a number'))
except:
    print('invalid number')


while True:
    try:
        number1=int(input('enter a number'))
    except:
        print('please provide a number')
        continue
    else:
        print('yes thank you')
        break