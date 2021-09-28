from datetime import datetime
from student import Student
from os import path
class User:
    def issue(self,id):
        if path.exists("BookMng.txt"):
            with open ("BookMng.txt","r") as fp:
                data=[]
                found= False
                k=Student()
                o="n"
                u="n"
                for line in fp:
                    try:
                        line.index(str(id),0,4)
                        c=line.split(",")
                        d=line.split(",")
                        if len(c)==5:
                            print("Sorry!!,Book is already issued...")
                            u="y"
                            break
                        if len(d)<4:
                            d[-1]=d[-1].strip("\n")
                        p=int(input("Enter student ID "))
                        i=k.searching(p)
                        if i=="y":
                            p=str(p)
                            d.append(p)
                            g=input("Enter issue Data(d-m-yyyy) ")
                            d.append(g)
                            d[-1]+="\n"
                            print("Book Issued...")
                            found= True
                        if i=="n":
                            print("Sorry!!,Invalid Student ID..")
                            o="y"
                            break
                        line=",".join(d)
                    except:
                        pass
                    data.append(line)
            if found:
                with open("BookMng.txt","w") as fp:
                    for i in data:
                        fp.write(i)
            if found==False:
                if o=="y"or u=="y":
                    pass
                else:
                    print("Sorry!!,Invalid Book ID..")
        else:
            print("Sorry!!,Invalid Book ID..")
        
    def submit(self,id):
        if path.exists("BookMng.txt"):
            with open("BookMng.txt","r") as fp:
                data =[]
                found= False
                for line in fp:
                    try:
                        line.index(str(id),0,4)
                        found= True
                        c=line.split(",")
                        d=line.split(",")
                        if len(c)==3:
                            print("Sorry!!, Book is not issued..")
                        if len(d)==5:
                            x=d[-1].split("-")
                            x[-1]=x[-1].strip("\n")
                            p=input("Enter Submit date(d-m-yyyy) ")
                            p=p.split("-")
                            f=datetime(int(x[2]),int(x[1]),int(x[0]))
                            o=datetime(int(p[2]),int(p[1]),int(p[0]))
                            dat=o-f
                            findat=dat.days
                            xf=findat-0
                            diff=findat-5
                        if xf<=5:
                            ans=input("Do you want to submit? ")
                        if diff>=1:
                            fine=diff*5
                            print("Please Pay fine of",fine,"Rs.")
                            ans=input("Do you want to submit? ")
                        if ans.lower()=="y":
                            d.remove(d[-1])
                            d.remove(d[-1])
                            d[-1]+="\n"
                            print("Book Submitted...")
                        line=",".join(d)
                    except:
                        pass
                    data.append(line)
            if found:
                with open("BookMng.txt","w+") as fp:
                    for i in data:
                        fp.write(i)
            else:
                print("Sorry!!,Invalid Book ID")
        else:
            print("Sorry!!,Invalid Book ID")
    
    def Addstudent(self):
        a=Student()
        k= a.acceptstd()
        if k:
            x=str(a)
            with open("student.txt","a") as fp:
                fp.write(x)
                fp.write("\n")
                print("Added Successfully!!!")
            
    def Displaystd(self):
        if path.exists("student.txt"):
            with open ("student.txt","r") as fp:
                for line in fp:
                    c=line.split(",")
                    print("--------------")
                    print("Student ID-",c[0])
                    print("Student Name-",c[1])
                    print("Student Class-",c[2])
                    print("Student Roll.No-",c[3])
                    print("--------------")
        else:
            print("Please, Add Students in system..")
    def Searchstd(self,id):
        if path.exists("student.txt"):
            with open("student.txt","r") as fp:
                for line in fp:
                    try:
                        line.index(str(id),0,4)
                        c=line.split(",")
                        print("--------------")
                        print("Student ID-",c[0])
                        print("Student Name-",c[1])
                        print("Student Class-",c[2])
                        print("Student Roll.No-",c[3])
                        print("--------------")
                        break
                    except:
                        pass
                else:
                    print("Sorry!!,Invalid Student ID..")
        else:
            print("Sorry!!,Invalid Student ID..")
        
    def Editstd(self,id):
        if path.exists("student.txt"):
            with open("student.txt","r") as fp:
                data=[]
                found= False
                for line in fp:
                    try:
                        line.index(str(id),0,4)
                        d = line.split(",")
                        print("--------------")
                        print("Student ID-",d[0])
                        print("Student Name-",d[1])
                        print("Student Class-",d[2])
                        print("Student Roll.No-",d[3])
                        print("--------------")
                        found= True
                        ans=input("Do you want to change the Name? ")
                        if ans.lower()=="y":
                            d[1]=input("Enter Name_").upper()
                        ans=input("Do you want to change the Class? ")
                        if ans.lower()=="y":
                            d[2]=input("Enter Class_").upper()
                        ans=input("Do you want to change the Roll.no? ")
                        if ans.lower()=="y":
                            d[3]=int(input("Enter Roll.no_"))
                            d[3]=str(d[3])
                            d[3]+="\n"
                        line=",".join(d)
                    except:
                        pass
                    data.append(line)
            if found:
                with open("student.txt","w") as fp:
                    for i in data:
                        fp.write(i)
            else:
                print("Sorry!!,Invalid Student ID")
        else:
            print("Sorry!!,Invalid Student ID..")
    def Deletestd(self,id):
        if path.exists("student.txt"):
            with open("student.txt","r") as fp:
                data=[]
                found= False
                for line in fp:
                    line.strip("\n")
                    try:
                        line.index(str(id),0,4)
                        found= True
                        d = line.split(",")
                        print("--------------")
                        print("Student ID-",d[0])
                        print("Student Name-",d[1])
                        print("Student Class-",d[2])
                        print("Student Roll.No-",d[3])
                        print("--------------")
                    except:
                        data.append(line)
            if found:
                ans=input("Do you want to delete student data?")
                if ans.lower()=="y":
                    with open("student.txt","w") as fp:
                        for e in data:
                            fp.write(e)
                        print("Student Data Delected...")
            else:
                print("Sorry!!,Invalid Student ID..")
        else:
            print("Sorry!!,Invalid Student ID..")
                        
if __name__=="__main__":
    s=User()
    s.Addstudent()
    s.Addstudent()
    s.Addstudent()
    



    
      





