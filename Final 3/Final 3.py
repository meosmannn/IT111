import sqlite3
import csv

conn = sqlite3.connect("test.db")
print("\nDatabase connected.")

conn.execute('''DROP TABLE IF EXISTS CONTACTS''')
conn.execute('''CREATE TABLE IF NOT EXISTS CONTACTS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         EMAIL          TEXT);''')
print("Table created.")

conn.execute("INSERT OR IGNORE INTO CONTACTS (ID,NAME, AGE,ADDRESS, EMAIL) \
      VALUES (10, 'Polly', 32, 'Seattle', 'polly@example.com')");
conn.execute("INSERT or IGNORE INTO CONTACTS (ID,NAME, AGE,ADDRESS, EMAIL) \
     VALUES (11, 'Roger', 28, 'Bainbridge', 'roger@example.com')");
conn.execute("INSERT or IGNORE INTO CONTACTS (ID,NAME, AGE,ADDRESS, EMAIL) \
     VALUES (12, 'Sam', 35, 'Bellevue', 'sam@example.com')");
conn.commit()
print("Records created. \n")

cursor = conn.execute("SELECT * from CONTACTS")
print("RECORDS:")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print("AGE = ", row[2])
   print ("ADDRESS = ", row[3])
   print ("EMAIL = ", row[4], "\n")

query = input("Enter a query term. Must be the ID.")
column = input("Enter a column name. Must be one of the following: ID, NAME, AGE, ADDRESS, EMAIL")

try:
    cursor = conn.execute(f"SELECT * from CONTACTS where {column} = '{query}'")
    print("\nSELECTED RECORD:")
    for row in cursor:
        print ("ID = ", row[0])
        print ("NAME = ", row[1])
        print("AGE = ", row[2])
        print ("ADDRESS = ", row[3])
        print ("EMAIL = ", row[4], "\n")
except Exception as e:
    print("Query not valid. Please check your input.")

cursor = conn.execute("SELECT * from CONTACTS")
data_list = []
for row in cursor:
   data_list.append(row)
print("RECORDS LIST:")
print(data_list)

filename = input("Enter the name of the CSV file for data export (without .csv extension): ")
filename = filename + ".csv"

with open(filename, mode='w') as contact_file:
    contact_writer = csv.writer(contact_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data_list:
        contact_writer.writerow(row)

print(f"\nCSV EXPORT COMPLETE. The data has been saved to {filename}")