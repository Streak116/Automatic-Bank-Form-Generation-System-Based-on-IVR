import sqlite3

# connecting to the database
connection = sqlite3.connect("accounts_db.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database

'''acc={
    '8985438536':{'Name':'Streak','Branch':'VSKP'},
    '8919776048':{'Name':'Tony Stark','Branch':'VZM'}'''

'''
sql_command = """CREATE TABLE accounts (acc_num VARCHAR(11),name VARCHAR(30),branch VARCHAR(15));"""
crsr.execute(sql_command)

com="insert into accounts values('08985438536','Streak','VSKP')"
crsr.execute(com)
com="insert into accounts values('08919776048','Mohammed Imran','VZM')"
crsr.execute(com)
com="insert into accounts values('08639090512','M. J. ROHIT VARMA','VSKP')"
crsr.execute(com)
com="insert into accounts values('09515860658','K. HARSHITHA','VZM')"
crsr.execute(com)
com="insert into accounts values('09603939185','SATYA KUMARI','VZM')"
crsr.execute(com)
com="commit"
crsr.execute(com)
'''

acc='08919776048'
com="select * from accounts"
# execute the statement
crsr.execute(com)
ans = crsr.fetchall()
print(ans)
for i in ans:
    if acc in i:
        print(i)
        name=i[1]
        acc_num=i[0]
        branch=i[2]
        
print(acc_num)
print(name)
print(branch)
# close the connection
connection.close()
