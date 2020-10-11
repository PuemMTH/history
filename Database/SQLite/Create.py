import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
# c.execute('''CREATE TABLE py_data (
#                 id int(11) NOT NULL,
#                 Username varchar(255) NOT NULL,
#                 Email varchar(255) NOT NULL,
#                 City varchar(255) NOT NULL
#                 )''')
# c.execute("INSERT INTO dks_login VALUES (NULL, 'PuemMTH', 'tcgamer.061@gmail.comasd', 'หนองกระทุ่ม')")
# c.execute("INSERT INTO py_data VALUES ('Six','tcgamer.061@gmail.com','0616544123','หนองกระทุ่ม')")
# c.execute("INSERT INTO `py_data` (`id`, `Username`, `Email`, `City`) VALUES (NULL, 'PuemMTH', 'tcgamer.061@gmail.comasd', 'หนองกระทุ่ม')")
c.execute('''CREATE TABLE py_data(
    Number varchar(255) NOT NULL, 
    Name varchar(255) NOT NULL, 
    Email varchar(255) NOT NULL)''')
    
for row in c.execute('SELECT * FROM py_data'):
        print(row)
conn.commit()

conn.close()