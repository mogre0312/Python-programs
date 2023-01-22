for num in range(1,51):
    if num%3==0 and num%5==0:
        print(str(num) +'=FizzBuzz')
    elif num%5==0:
        print(str(num) +'=Buzz')
    elif num%3==0:
        print(str(num) +'=Fizz')
    else:
        print(num)


