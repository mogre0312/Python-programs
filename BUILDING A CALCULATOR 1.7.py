num1=float(input('enter first num'))
operator=(input('enter operator'))
num2=float(input('enter second num'))
if operator=='+':
    print(num1+num2)
elif operator=='-':
    print(num1-num2)
elif operator=='*':
    print(num1*num2)
else: print('invalid operator')