import os
print(os.listdir())
simple = "asde%s"%(".puem")
list_of_files = os.listdir()
if simple in list_of_files:
    print("simple in file")
    file1 = open(simple, "r")
    verify = file1.read().splitlines()
else:
      print("user_not_found")