import sqlite3

# defining connection and cursor
conn = sqlite3.connect('vehicles.db')
cursor = conn.cursor()

# creating cars table
query = """CREATE TABLE IF NOT EXISTS
cars(car_name CHAR(20) PRIMARY KEY NOT NULL,
 owner_name CHAR(20) NOT NULL)"""
cursor.execute(query)
# data collection 
for i in range(0, 10):
    car = input("Car name:").lower().capitalize()
    owner = input("Owner name:").lower().capitalize()
conn.execute("INSERT INTO cars (car_name,owner_name) " "VALUES(?, ?)", (car, owner))
cursor.execute("SELECT car_name,owner_name  FROM cars")
results = cursor.fetchall()
print(results)
