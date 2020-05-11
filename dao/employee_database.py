import sqlite3

conn = sqlite3.connect('company.db')
print ("Opened database successfully")


conn.execute('''CREATE TABLE EMPLOYEE
         (ID    INT PRIMARY KEY  ,
          NAME  TEXT NOT NULL,
          AGE INT NOT NULL,
          ADDRESS TEXT NOT NULL, 
          SALARY INT NOT NULL);''')

conn.execute('''CREATE TABLE TECH
         (ID    INT PRIMARY KEY  ,
          NAME  TEXT NOT NULL,
          DOMAIN TEXT NOT NULL);''')

conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");


conn.execute("INSERT INTO TECH (ID,NAME,DOMAIN) \
      VALUES (1, 'Paul', 'Python')");

conn.execute("INSERT INTO TECH (ID,NAME,DOMAIN) \
      VALUES (2, 'Allen', 'Java')");

conn.execute("INSERT INTO TECH (ID,NAME,DOMAIN) \
      VALUES (3, 'Teddy', 'PHP')");

conn.execute("INSERT INTO TECH (ID,NAME,DOMAIN) \
      VALUES (4, 'Mark', 'Testing')");



conn.commit()
print("Records created successfully");
conn.close()
