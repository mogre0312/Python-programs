class chef():
    def makechicken(self):
        print('the chef makes chicken')
    def makesalad(self):
        print('the chef makes salad')
    def makesoup(self):
        print('the makes soup')
chef1=chef()
chef1.makechicken()
chef1.makesalad()
chef1.makesoup()
class chinesechef(chef):
    def makesfriedrice(self):
        print('the chinese chef makes fried rice')
chef2=chinesechef()
chef2.makesfriedrice()
chef2.makechicken()