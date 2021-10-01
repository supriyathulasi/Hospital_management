import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="root",database="hospital")
def add(patid,patname,phone,gender,age,addr,pw):
    query="insert into add_pat(patid,patname,phone,gender,age,address,password) values({},'{}',{},'{}',{},'{}','{}')".format(patid,patname,phone,gender,age,addr,pw)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print("patient added")
def see():
    query="select * from add_pat"
    cur=con.cursor()
    cur.execute(query)
    for row in cur:
        print("patient_id:",row[0])
        print("patient_name:",row[1])
        print("phone:",row[2])
        print("gender:",row[3])
        print("age:", row[4])
        print("address:", row[5])
        print("password:",row[6])
        print()
        print()
def delete(id):
    query="delete from add_pat where patid={}".format(id)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print("record deleted")
def update(id, name, phonenum, gender, age, addr, pw):
    res = con.cursor()
    sql = "update add_pat set patname=%s,phone=%s,gender=%s,age=%s,address=%s,password=%s where patid=%s"
    user = (name, phonenum, gender, age, addr, pw,id)
    res.execute(sql,user)
    con.commit()
    print("successfully updated!")
# def appoint(id,docname,time):
#     cur = con.cursor()
#     query = "insert into appointment(id,dname,timing) values({},'{}','{}')".format(id, docname, time)
#     cur.execute(query)
#     con.commit()
#     print("appointment fixed")
#     cur = con.cursor()
#     query = "select dname,timing from appointment where id={}".format(id)
#     cur.execute(query)
#     db = cur.fetchone()
#     d = list(db)
#     a = d[0]
#     b=d[1]
#     if(docname==a and time==b):
#         print("appointment cancelled")


def cancel_appoint(id):
    query = "delete from appointment where id={}".format(id)
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    print("appointment cancelled!")

def admin(id_no,password):
    cur=con.cursor()
    query="select password from admin where id={}".format(id_no)
    cur.execute(query)
    db=cur.fetchone()
    d=list(db)
    a=d[0]
    if(password==a):
        print("login successfull")
        print("enter 0 to add patient")
        print("enter 1 to see details")
        print("enter 2 to delete patient record")
        print("enter 3 to edit patient record")
        choice = int(input("enter choice"))
        if (choice == 0):

            id = int(input("enter patient id"))
            name = input("enter patient name")
            phone = input("enter phone number")
            gender=input("enter gender")
            age=int(input("enter age"))
            addr=input("enter address")
            pw=input("enter password")
            add(id, name, phone, gender, age, addr, pw)
        elif(choice==1):
            see()
        elif(choice==2):
            id=int(input("enter patient's id to delete"))
            delete(id)
        elif(choice==3):
            id=int(input("enter patient id"))
            name=input("enter patient name")
            phone=int(input("enter phone number"))
            gender = input("enter gender")
            age = int(input("enter age"))
            addr = input("enter address")
            pw = input("enter password")
            update(id, name, phone, gender, age, addr, pw)

    else:
        print("invalid")

def user(id_no,password):
    cur=con.cursor()
    query="select password from add_pat where patid={}".format(id_no)
    cur.execute(query)
    db=cur.fetchone()
    d=list(db)
    a=d[0]
    if(password==a):
        print("login successfull for user")
        print("enter 1 to see details")
        print("enter 2 to edit patient record")
        print("enter 3 to fix appointment")
        print("enter 4 to cancel appointment")
        print("enter 5 to pay fees")
        choice = int(input("enter choice"))
        if (choice == 1):
            see()
        if(choice==2):
            id = int(input("enter patient id"))
            name = input("enter patient name")
            phone = int(input("enter phone number"))
            gender = input("enter gender")
            age = int(input("enter age"))
            addr = input("enter address")
            pw = input("enter password")
            update(id, name, phone, gender, age, addr, pw)
        if(choice==3):
            print("DR-VINISHA DENTAL")
            print("DR-SRINIVASAN ORTHO")
            print("DR-GOKUL CARDIOLOGIST")
            print("DR-MANIMARAN ENT")
            print("DR-SUGANTHI GENERAL")
            print("DR-ASHWIN SURGERY")
            id=int(input("enter your id"))
            doc=input("enter doctor name")
            time=input("enter timing for appointment")
            if (doc == "vinisha"):
                bill = 200
            elif (doc == "srinivasan"):
                bill = 150
            elif (doc == "gokul"):
                bill = 300
            elif(doc=="manimaran"):
                bill=400
            elif(doc=="suganthi"):
                bill=350
            cur = con.cursor()
            query = "insert into appointment(id,dname,timing,bill) values({},'{}','{}',{})".format(id, doc, time,bill)
            cur.execute(query)
            con.commit()

            cur = con.cursor()
            query = "select dname,timing from appointment where id={}".format(id)
            cur.execute(query)
            db = cur.fetchone()
            d = list(db)
            a = d[0]
            b = d[1]
            if (doc == a and time == b):
                print("appointment cancelled")



    if(choice==4):
            id=int(input("enter your id to cancel appointment"))
            cancel_appoint(id)
    if(choice==5):

            id=int(input("enter id to pay fee"))
            print("enter 1 for credit card")
            print("enter 2 for debit card")
            ch=int(input("enter your choice"))
            if(ch==1):
                code=int(input("enter ifsc code"))
                acnum=int(input("enter acnum"))
                cur=con.cursor()
                query="select bill from appointment where id={}".format(id)
                cur.execute(query)
                db=cur.fetchone()
                d=list(db)
                a=d[0]
                print(a)

                print("your bill is ", a)
            elif(ch==2):
                acnum=int(input("enter acc number"))
                code=int(input("enter code"))
                cur = con.cursor()
                query = "select bill from appointment where id={}".format(id)
                cur.execute(query)
                db = cur.fetchone()
                d = list(db)
                a = d[0]
                print("your bill is",a)




def view():
    query="select * from add_pat"
    cur=con.cursor()
    cur.execute(query)
    for row in cur:
        print("patient_id:",row[0])
        print("patient_name:",row[1])
        print("phone:",row[2])
        print("gender:",row[3])
        print("age:", row[4])
        print("address:", row[5])
        print("password:",row[6])
        print()
def main():
    while True:
        print("*****************************************")
        print("|Enter 1 for Admin mode |\n|Enter 2 for user mode |")
        print("******************************************")
        mode = int(input("enter mode:"))
        if mode==1:
            id = int(input("enter id"))
            pw = input("enter password")
            admin(id, pw)
        elif mode==2:
            id = int(input("enter id"))
            pw = input("enter password")
            user(id,pw)


main()



