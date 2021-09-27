import sqlite3

# defining connection and cursor
conn = sqlite3.connect('Python.db')
cursor = conn.cursor()


#CREATING HOSPITAL TABLE
query = """CREATE TABLE IF NOT EXISTS
Hospital(hospital_id INTEGER ,
     hospital_name TEXT ,
     bed_count INTEGER )"""
cursor.execute(query)

cursor.execute("INSERT INTO Hospital VALUES('1', 'Mayo Clinic', 200)")
cursor.execute("INSERT INTO Hospital VALUES('2', 'Cleveland Clinic', 400)")
cursor.execute("INSERT INTO Hospital VALUES('3', 'Johns Hopkins', 1000)")
cursor.execute("INSERT INTO Hospital VALUES('4', 'UCLA Medical Center', 1500)")
#creating doctor table
query = """CREATE TABLE IF NOT EXISTS 
Doctor (doctor_id INTEGER ,
     doctor_name TEXT ,
     hospital_id INTEGER ,
     joining_date TEXT ,
     speciality TEXT ,
     salary INTEGER ,
     experience INTEGER
)"""
cursor.execute(query)

cursor.execute("INSERT INTO Doctor VALUES('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL)")
cursor.execute("INSERT INTO Doctor VALUES('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL)")

def get_connection():
    connection = sqlite3.connect('Python.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

print(" Read given hospital and doctor details \n")

specftn = input("Speciality:").lower().capitalize()
salary = input("Salary:")
query= """SELECT * from DOCTOR WHERE SPECIALITY = ? AND SALARY>= ?"""
cursor.execute(query, (specftn, salary))
record = cursor.fetchall()
for row in record:
    print("Doctor_Id: ", row[0])
    print("Doctor_Name:", row[1])
    print("Hospital_Id:", row[2])
    print("Joining Date:", row[3])
    print("Specialty:", row[4])
    print("Salary:", row[5])
    print("Experience:", row[6], "\n")
print("\n")
hospital_id = input("Select ID for info:")
select_query = """SELECT * from HOSPITAL WHERE HOSPITAL_ID = ?"""
cursor.execute(select_query, (hospital_id,))
records = cursor.fetchone()
hospdetails= records[1]
sql_ = """SELECT * from DOCTOR WHERE HOSPITAL_ID = ?"""
cursor.execute(sql_,(hospital_id) )
record = cursor.fetchall()
for row in record:
    print("Doctor Name:", row[1])
    print("Hospital Id:", row[2])
    print("Hospital name",hospdetails, "\n")


conn.commit()
conn.close()