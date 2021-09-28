from user import User
a=User()
def MainUser():
    choice=0
    while choice!=8:
        print("""\t\t 1. Issue Book
    \t\t 2. Submit Book
    \t\t 3. Display All Student
    \t\t 4. Add New Student
    \t\t 5. Search Student
    \t\t 6. Edit Student Data
    \t\t 7. Delete Student Data
    \t\t 8. Exit""")
        choice=int(input("Enter your choice_"))
        if choice==1:
            id=int(input("Enter Book ID_"))
            a.issue(id)
        elif choice==2:
            id=int(input("Enter Book ID_"))
            a.submit(id)
        elif choice==3:
            a.Displaystd()
        elif choice==4:
            a.Addstudent()
        elif choice==5:
            id=int(input("Enter Student ID to Search_"))
            a.Searchstd(id)
        elif choice==6:
            id=int(input("Enter Student ID to Edit_"))
            a.Editstd(id)
        elif choice==7:
            id=int(input("Enter Student ID to Delet_"))
            a.Deletestd(id)
        elif choice==8:
            print("Exit")
if __name__=="__main__":
    MainUser()


