from os import path
class Book:
    def accept(self):
        self.id= int(input("Enter Book ID "))
        ask="y"
        if path.exists("BookMng.txt"):
            with open("BookMng.txt","r") as fp:
                for line in fp:
                    try:
                        line.index(str(self.id),0,4)
                        print("Sorry!!, ID already exist")
                        ask="n"
                        break
                    except:
                        pass
        if ask=="y":
            self.name= input("Enter Book Name ").upper()
            self.auther= input("Enter Book Auther ").upper()
            return True
                
    def __str__(self):
        data=str(self.id)
        data+=","+(self.name)
        data+=","+(self.auther)
        return data
if __name__=="__main__":
    d=Book()
    c=d.accept()
    if c : 
        print(d)

