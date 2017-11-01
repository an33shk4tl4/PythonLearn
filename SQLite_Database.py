import sqlite3

conn = sqlite3.connect('enterprise.db')



curs = conn.cursor()
x = curs.execute('drop table zoo')
print type(x)
print curs.rowcount

curs.execute('''create table zoo 
(critter varchar(20) primary key,
count int,
damages float)''')
print curs.rowcount

curs.execute('insert into zoo values("duck", 5, 0.0)')
print curs.arraysize
curs.execute('insert into zoo values("bear", 2, 1000.0)')

print curs.rowcount
ins = 'insert into zoo (critter,count, damages) values(?,?,?)'

curs.execute(ins, ('weasel', 1, 2000.0))
print curs.arraysize

curs.execute('select * from zoo')
print curs.arraysize

rows = curs.fetchall()
print curs.arraysize
print(rows)

curs.execute('select * from zoo order by count')
print(curs.fetchall())

curs.close()
conn.close()
