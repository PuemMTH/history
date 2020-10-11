def Circumference(pi):
    radius = float(input("radius : "))
    return pi * (radius ** 2)
def Exponent(Number,Ex):
    return Number ** Ex
logn = 30
print("██████████████████████████████")
print("█                            █")
print("█        Cr.PuemMTH          █")
print("█     Circumference : a      █")
print("█     Exponent : b           █")
print("█                            █")
print("██████████████████████████████")
key = str(input("Run function : "))
if key == "a":
    pi = 3.14
    print("Ans circumference: ",Circumference(pi))
elif key == "b":
    Number = float(input("Number : "))
    Ex = float(input("Exponent : "))
    print("Ans exponent: ",Exponent(Number,Ex))
elif key == "n":
    raise SystemExit
else:
    raise SystemExit