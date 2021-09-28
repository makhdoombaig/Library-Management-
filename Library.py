from mainuser import MainUser
from mainadmin import Mainadmin
choice=0
while choice!=3:
    print("""\t\t 1. Admin Section
    \t\t 2. User Section
    \t\t 3. Exit""")
    choice=int(input("Enter your choice_"))
    if choice==1:
        Mainadmin()
    if choice==2:
        MainUser()
    if choice==3:
        break


