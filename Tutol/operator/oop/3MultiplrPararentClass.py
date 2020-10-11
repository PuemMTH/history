class FasterClass:
    gender = "Male"
    def SayHello(self):
        print("Hello Faster !")
    def SayHi(self,fname,lname):
        print("Hi! %s %s"%(fname,lname))
    def Hiv(self):
        print("Hiv")
class MomClass:
    sex = "Female"
    def SayNO(self):
        print("Hello mon !")     
class ChildClass(FasterClass,MomClass):
    def SayObj(self):
        print("Staff")
c1 = ChildClass()
c1.SayNO()
c1.SayHi("Tanapath","Eiam-Arj")