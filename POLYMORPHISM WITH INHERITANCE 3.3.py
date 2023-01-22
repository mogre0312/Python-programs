class bird():
    def intro(self):
        print('there are many types of birds')
    def flight(self):
        print('some bird cant fly')

class ostrich(bird):
    def flight(self):
        print('ostrich cant fly')
class sparrow(bird):
    def flight(self):
        print('sparrow can fly')

Bird=bird()
ost=ostrich()
spa=sparrow()
Bird.intro()
ost.flight()
spa.flight()