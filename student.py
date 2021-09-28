from os import path
class Student:
    def acceptstd(self):
        self.id= int(input("Enter Student ID- "))
        ask="y"
        if path.exists("student.txt"):
            with open("student.txt","r") as fp:
                for line in fp:
                    try:
                        line.index(str(self.id),0,4)
                        print("Sorry!!,ID already exist")
                        ask="n"
                        break
                    except:
                        pass
        if ask=="y":
            self.name=input("Enter Student Name- ").upper()
            self.clas=input("Enter Student Class (year,banch&Div)- ").upper()
            self.roll=input("Enter your class roll.no- ")
            
            return True
    def searching(self,id):
        if path.exists("student.txt"):
            with open("student.txt","r") as fp:
                f="n"
                for i in fp:
                    try:
                        i.index(str(id),0,4)
                        f="y"
                    except:
                        pass
                return f
                    
    def __str__(self):
        data=str(self.id)
        data+=","+self.name
        data+=","+self.clas
        data+=","+str(self.roll)
        return data
if __name__=="__main__":
    a=Student()
    c = int(input("Student ID please "))
    i=a.searching(c)
    print(i)


        
            



