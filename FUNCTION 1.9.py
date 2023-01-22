def say_hi(name):
    print('Hello'  + name)
say_hi('pooja')

#find the max number
def max(num1, num2, num3):
    if num1>num2 and num1>num3:
        print('num1 is greater')
    elif num2>num1 and num2>num3:
        print('num2 is greater')
    else:
        print('num3 is greater')
max(999,200,10)
