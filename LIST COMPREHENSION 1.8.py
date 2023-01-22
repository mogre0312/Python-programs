x='pooja'
list=[letters for letters in x]
print(list)

number=[num for num in range(1,10)]
print(number)

#numbers divisible by 3
num1=[num for num in range(1,50) if num%3==0]
print(num1)

#even numbers list
num2=[num for num in range(1,100) if num%2==0]
print(num2)

#square root
num3=[num**2 for num in range(1,50)]
print(num3)

#create a sqaure root divisible by 3
num4=[num**2 for num in range(1,50) if num%3==0]
print(num4)

string='print every word in this sentence that has even number of letters'
for word in string.split():
    if len(word)%2==0:
        print(word + 'is even')

string1='sam print only the words that starts with s in this sentence'
for word in string.split():
    if word[0]=='s':
        print(word + 'starts with s')

