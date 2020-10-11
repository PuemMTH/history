import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
# c.execute('''CREATE TABLE dks_login
#              (email text, password text, phone text, sex text)''')
c.execute("INSERT INTO dks_login VALUES ('tcgamer.061@gmail.com','tcgamer.061','0616544123','male')")
# for row in c.execute('SELECT * FROM dks_login'):
#         print(row)
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()