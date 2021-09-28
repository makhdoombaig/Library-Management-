from user import User
from book import Book
from os import path
class Admin:
    def AddBook(self):
        d=Book()
        c= d.accept()
        if c:
            f=str(d)
            with open("BookMng.txt","a") as fp:
                fp.write(f)
                fp.write("\n")
                print("Added Successfully!!!")
                    
    def Display(self):
        if path.exists("BookMng.txt"):
            with open("BookMng.txt","r") as fp:
                for line in fp:
                    c=line.split(",")
                    print("")
                    print("Book ID-",c[0])
                    print("Book Name-",c[1])
                    print("Book Auther-",c[2])
                    print("--------------")
        else:
            print("Please Add Books in system...")
    def Search(self,eid):
       if (path.exists("BookMng.txt")):
            with open("BookMng.txt","r") as fp:
                for line in fp:
                    try:
                        line.index(str(eid),0,4)
                        c =line.split(",")
                        d =line.split(",")
                        if len(c)>3:
                            print("Sorry!!,Book is already Issued by..")
                            d=c[-2]
                            a=User()
                            a.Searchstd(d)
                        if len(d)==3:
                            print("--------------")
                            print("Book ID-",c[0])
                            print("Book Name-",c[1])
                            print("Book Auther-",c[2])
                            print("--------------")
                            break
                    except:
                        pass
                else:
                    print("Please!.Enter a valid Book ID.")
       else:
            print("Please!.Enter a valid Book ID.")
    def Edit(self,eid):
        if path.exists("BookMng.txt"):
            with open("BookMng.txt","r") as fp:
                data=[]
                found= False
                for line in fp:
                    try:
                        line.index(str(eid),0,4)
                        found= True
                        d=line.split(",")
                        print("Book ID-",d[0])
                        print("Book Name-",d[1])
                        print("Book Auther-",d[2])
                        print("--------------")
                        ans=input("Do you want to change the Book name ?")
                        if ans.lower()== "y":
                            d[1]=input("Enter Name_").upper()
                        ans=input("Do you want to change the Auther name ?")
                        if ans.lower()=="y":
                            d[2]=input("Enter Auther Name_").upper()
                            d[2]+="\n"
                        line=",".join(d)
                    except:
                        pass
                    data.append(line)
                
            if found:
                with open("BookMng.txt","w") as fp:
                    for i in data:
                        fp.write(i)
            else:
                print("Please!.Enter a valid Book ID..")
        else:
            print("Please!.Enter a valid Book ID..")
                    
    def Delet(self,eid):
        if path.exists("BookMng.txt"):
            with open("BookMng.txt","r") as fp:
                data=[]
                found= False
                for line in fp:
                    line.strip("\n")
                    try:
                        line.index(str(eid),0,4)
                        found= True
                        d=line.split(",")
                        print("Book ID-",d[0])
                        print("Book Name-",d[1])
                        print("Book Auther-",d[2])
                    except:
                        data.append(line)   
            if found:
                ans=input("Do you want to delete book ?")
                if ans.lower()=="y":
                    with open ("BookMng.txt","w") as fp:
                        for e in data: 
                            fp.write(e)
                        print("Book Data Delected...")
            else:
                print("Please!.Enter a valid Book ID..")
        else:
            print("Please!.Enter a valid Book ID..")
            
if __name__=="__main__":
    a=Admin()
    a.AddBook()
    a.AddBook()
    a.AddBook()
    a.AddBook()
    a.Display()
    c=int(input("enter Book id"))
    a.Search(c)
