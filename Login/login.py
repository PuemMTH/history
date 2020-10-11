Users={}
Status=""
def Status_user():
    Status=input("New User press 'n'\told users press'y'\tExit press 'q'\nPress : ")
    if Status == 'n':
        newUser()
    elif Status == 'y':
        oldUser()
def newUser():
    CreateID = input("Create Username : ")
    if CreateID in Users:
        print("ID Online Exit!")
    else:
        CreatePass = input("Create Password : ")
        Users[CreateID] = CreatePass
        print("Created")
def oldUser():
    Login = input("ID : ")
    Password = input("Password : ")
    if Login in Users and Users[Login]==Password:
        print("Login seccesfull")
    else:
        print("wrong ID or Password!")
while Status != 'q':
    print(Users)
    Status_user()
                       
