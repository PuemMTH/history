class ParentClass:
    name = "Circle"
    size = 400
    r = 20
    def SayHello(self):
        print("Hello")
    def SayHi(self,fname,lname):
        print("Hi! %s %s"%(fname,lname))
    def Hiv(self):
        print("Hiv")
class ChildClass(ParentClass): #สืบทอด class มาจาก ParentClass
    def SayObj(self):
        print("Staff")
c1 = ChildClass()
c1.SayHi("Tanapat","Eiam-ary")
c1.Hiv()
print(c1.name)