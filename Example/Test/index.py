class Player:
    def createName(self,sname,lname):
        self.sname = sname
        self.lname = lname
    def displayname(self):
        return ("{} {}".format(self.sname,self.lname))
if __name__ == '__main__':
    p1 = Player()
    p1.createName("Thanapath","Eiam-arj")
    p2 = Player()
    p2.createName("Piyamas","papukdee")
    print("{}\n{}".format(p1.displayname(),p2.displayname()))