x='pooja'
for letters in x:
    print(letters)
friends=['pooja','sunidhi','nidhi']
for elements in friends:
    print(elements)
for num in range(1,10):
    print(num)
for number in range(5):
    print(number)

#to replace vowels
word=input('enter a word')
for i in word:
    if i in 'aeiou':
        word=word.replace(i,'g')
print(word)