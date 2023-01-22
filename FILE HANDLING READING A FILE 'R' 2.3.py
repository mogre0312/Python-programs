person_file=open('file.txt','r')
print(person_file)
#person_file.close()
#print(person_file.read())
#print(person_file.readable())
#print(person_file.readlines()[0])

for person in person_file:
    print(person)