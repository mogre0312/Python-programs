import re

string='This is string! but it has punctuation. How can we remove it?'
print(re.findall('[^!.?]+',string))

string11=' Lets find how many Upper and lower case letters in this Sentence'
print(re.findall('[a-z]+',string11))
print(re.findall('[A-Z]+', string11))
print(re.findall('[a-z, A-Z]+', string11))
print(re.findall('[A-Z][a-z]+',string11))