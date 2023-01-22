def upper_lower(string):
    d={'upper':0, 'lower':0}
    for letter in string:
        if letter.isupper():
            d['upper']+=1
        elif letter.islower():
            d['lower']+=1
        else:
            pass
    print('no. of upper case letters', d['upper'])
    print('no. of lower case letters', d['lower'])
print(upper_lower('Hello this is Pune'))