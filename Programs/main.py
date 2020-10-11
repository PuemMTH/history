import os
import sys
import random
color = ['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
White = '\033[0m'
Green = '\033[1;32m'
Red = '\033[1;31m'
def clr():
    if os.name == 'nt':
        os.system('cls')
        os.system('title Currency converter by #PuemMTH')
    else:
        os.system('clear')
def money():
    print("█                                           █")
    print("█           Ampere * Volts = watt           █")
    print("█ watt * hour * Unit / Kilowatt-hour = Bath █")
    print("█                                           █")
    print("")
    Ampere = float(input("Ampere {A} : "))
    Volts = float(input("Volts {V} default 220V : "))
    hour = float(input("hour {H} default 24h : "))
    unit = float(input("Unit {U} default 4.2218u : "))
    return Ampere*Volts*hour*unit/1000
def main():
    key = str(input("Key : "))
    if key == "a":
        clr()
        print(money())
    elif key == "n":
        print(random.choice(color)+"Good bye ......"+White)
    elif key == "clr":
        clr()
    else:
        main()
main()
