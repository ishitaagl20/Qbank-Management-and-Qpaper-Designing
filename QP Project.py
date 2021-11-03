import pymysql
db=pymysql.connect(host="localhost",user="root",password="root")
mycur=db.cursor()
try:
    mycur.execute("Create Database Question")
    print("Database created...")
except:
    print("Database already exists...")
mycur.execute("Use Question")
try:
    mycur.execute("Create table Qbank(QID int primary key, \
Question varchar(1000), Qchapterno int, Qmarks int)")
    print("Table Qbank is created")
except:
    print("Table Qbank already exists...")

def addrecord():
    print("Entering values in the database...")
    print("Question's Id, chapterno and marks are integers")
    while True:
        qid=input("Enter the Question ID: ")
        question=input("Enter Question: ")
        qchap=input("Enter Chapter no: ")
        qmarks=input("Enter the marks that the question carries: ")
        record="Insert into Qbank values ("+qid+",'"+question+"',"+qchap+","+qmarks+")"
        mycur.execute(record)
        db.commit()
        choice=input("Do you want to enter more records (y/n): ")
        while choice not in ["Y","y","N","n"]:
            print("Inappropriate Input: ")
            choice=input("Enter your choice again: ")
        if choice in ["N","n"]:
            break

def viewall():
    mycur.execute("Select * from qbank")
    table=mycur.fetchall()
    for QID,Question,Qchapterno,Qmarks in table:
        print(QID,Question,"Chapterno:",Qchapterno,"Marks:",Qmarks)

def viewchapwise():
    mycur.execute("Select * from qbank")
    chapno=int(input("Enter the chapter whose questions to be searched: "))
    table=mycur.fetchall()
    for QID,Question,Qchapterno,Qmarks in table:
        if chapno==Qchapterno:
            print(QID,Question,"Marks:",Qmarks)
           
def qpaper_design():
    file=open("Question_paper.txt","w")
    sname=input("Enter school name: ")
    file.write(sname+"\n")
    ename=input("Enter exam name: ")
    file.write(ename+"\n"+"\n")
    no_q=int(input("Enter number of questions: "))
    mycur.execute("Select * from qbank")
    table=mycur.fetchall()
    qdet_list=[]
    for qno in range(1,no_q+1):
        while True:
            qno=str(qno)
            qchap=int(input("Enter the chapter number: "))
            qmarks=int(input("Enter question marks: "))
            qdet_tuple=(qchap,qmarks)
            qdet_list.append(qdet_tuple)
            count=qdet_list.count(qdet_tuple)
            qlist=[]
            for QID,Question,Qchapterno,Qmarks in table:
                if qchap==Qchapterno and qmarks==Qmarks:
                    qlist.append(Question)
            if len(qlist)>=count:
                file.write("Q"+qno+" "+qlist[count-1]+"\n")
                break
            else:
                print("Question not available, enter details again....")
    file.close()


    

print("Choice-1:Add Question")
print("Choice-2:View all questions")
print("Choice-3:View questions chapterwise")
print("Choice-4:Design the question paper")

while True:                                                        
    choice=int(input("Enter your choice: "))
    while choice not in [1,2,3,4]:
        print("Inappropriate input")
        choice=int(input("Enter your choice again(1/2/3/4): "))
    if choice==1:
        addrecord()
    elif choice==2:
        viewall()
    elif choice==3:            
        viewchapwise()
    elif choice==4:
        qpaper_design()
    check=input("Do you want to perform more functions (y/n): ")
    while check not in ["Y","y","N","n"]:
        print("Inappropriate input")
        check=input("Enter your choice again(y/n):")
    if check in ["n","N"]:
        break

    
    

            
                
                
                
                
            
        
    
    
        
        
    
    
