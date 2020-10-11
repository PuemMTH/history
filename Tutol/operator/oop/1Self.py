class Player:
    def createName(self,name):
        self.name = name
    def displayname(self):
        print("Hello!! %s"%self.name)

p1 = Player()
p2 = Player()
p3 = Player()

p1.createName("Wasana")
p2.createName("Piyamas")
p3.createName("Thanapath")

p1.displayname()
p2.displayname()
p3.displayname()
# obj.createName()