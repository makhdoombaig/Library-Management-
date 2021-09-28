from admin import Admin
def Mainadmin():
    a=Admin()
    choice=0
    while choice!=6:
        print("""\t\t 1. Add Book
    \t\t 2. Display All Books
    \t\t 3. Search Book
    \t\t 4. Edit Book
    \t\t 5. Delet Book
    \t\t 6. Exit""")
        choice=int(input("Enter your choice_"))
        if choice==1:
            a.AddBook()
        elif choice==2:
            a.Display()
        elif choice==3:
            i=int(input("Enter Book ID to Search_"))
            a.Search(i)
        elif choice==4:
            j=int(input("Enter Book ID to Edit_"))
            a.Edit(j)
        elif choice==5:
            k=int(input("Enter Book ID to Delete_"))
            a.Delet(k)
        elif choice==6:
            print("Exit")
            
if __name__=="__main__":
    Mainadmin()
