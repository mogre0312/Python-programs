import re

string='hello this is pune'
print(re.search('pune', string))
print(re.findall('pune',string))


string1='i think i know him, is that@rahul sarode'
split_term='@'
print(re.split('@',string1))

string2='very cold here'
print(re.sub('\s','p',string2))