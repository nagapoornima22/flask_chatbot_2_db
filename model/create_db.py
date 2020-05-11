import sqlite3

conn = sqlite3.connect('users.db')


conn.execute('''CREATE TABLE userdata
         (username           TEXT    NOT NULL,
          password            TEXT    NOT NULL);''')

print ("Table created successfully")

conn.execute("INSERT INTO userdata (username, password) \
      VALUES ('xyz','xyzpasswd' )");

conn.execute("INSERT INTO userdata (username, password) \
      VALUES ('pqr','pqrpasswd' )");


conn.execute("INSERT INTO userdata (username, password) \
      VALUES ('abc','abcpasswd' )");

conn.execute("INSERT INTO userdata (username, password) \
      VALUES ('def','defpasswd' )");


conn.commit()
print("Records created successfully");
conn.close()
