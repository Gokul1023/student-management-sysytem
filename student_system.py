import mysql.connector
connect=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gokul@1023",
    database="student_db"
)
cursor=connect.cursor()

def add_student():
    reg=input("Enter Register No: ")
    name=input("Enter Name: ")
    dept=input("Enter Department: ")
    year=int(input("Enter Year: "))

    query="insert into students(reg,name,department,year)" \
    "values(%s,%s,%s,%s)"
    data=(reg,name,dept,year)
    cursor.execute(query,data)
    connect.commit()
    print("Student Added Successfully!")

def view_students():
    cursor.execute("select * from students")
    result=cursor.fetchall()
    for i in result:
        print(i)

def search_students():
    reg=input("Enter Register No: ")
    cursor.execute("select * from student where reg_no=%s",reg)
    result=cursor.fetchone()
    print(result if result
          else"Student not Found")
    
def delete_students():
    reg=input("Enter Register No to Delete: ")
    cursor.execute("delete from students where reg_no=%s",reg)
    connect.commit()
    print("Student Deleted Successfully!")

while True:
    print("""
1.Add Student
2.View Students
3.Search Student
4.Delete Student
5.Exit
""")

    choice=int(input("Enter your choice: "))
    
    if choice==1:
        add_student()
    elif choice==2:
        view_students()
    elif choice==3:
        search_students()
    elif choice==4:
        delete_students()
    elif choice==5:
        print("Thank you!")
        break
    else:
        print("Invalid Choice")



