import mysql.connector
connect=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gokul@1023",
    database="student_db"
)
cursor=connect.cursor()

def add_student():
        reg_no = input("Enter Register Number: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        year = int(input("Enter Year: "))
        
        query = "INSERT INTO students (reg_no, name, department, year) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (reg_no, name, dept, year))
        print("✅ Student added successfully!")

def view_students():
    cursor.execute("select * from students ORDER by reg_no")
    result=cursor.fetchall()
    if result:
        print(f"\n{'Reg No':<15} {'Name':<20} {'Department':<20} {'Year':<10}")
        print("-" * 70)
        for row in result:
            print(f"{row[0]:<15} {row[1]:<20} {row[2]:<20} {row[3]:<10}")
        print(f"\nTotal: {len(result)} students")

def search_students():
    reg_no=input("Enter Register No: ")
    cursor.execute("select * from students WHERE reg_no=%s",(reg_no,))
    result=cursor.fetchone()
    if result:
            print(f"\nRegister No: {result[0]}")
            print(f"Name: {result[1]}")
            print(f"Department: {result[2]}")
            print(f"Year: {result[3]}")
    else:
            print("❌ Student not found!")
    
def delete_students():
    reg_no=input("Enter Register No to Delete: ")
    cursor.execute("delete from students where reg_no=%s",(reg_no,))
    connect.commit()
    print("Student Deleted Successfully!")

while True:
    print("""
***STUDENT MANAGEMENY SYSTEM***
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


