class dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + 'says woof'

class cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name + 'says meow'

mark=dog('mark')
lili=cat('lili')
print(mark.speak())
print(lili.speak())

#polymorphism using for loop

class india():
    def capital(self):
        print('Delhi is a capital of india')
    def language(self):
        print('Hindi is language of india')
    def type(self):
        print('India is developing country')

class usa():
    def capital(self):
        print('Washngton D.C. is capital of usa')
    def language(self):
        print('English is the language of usa')
    def type(self):
        print('USA is developed country')
india=india()
usa=usa()
for country in(india,usa):
    country.capital()
    country.language()
    country.type()

