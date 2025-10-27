from tkinter import *
import sqlite3
'''db=sqlite3.connect('db1.db')
cur=db.cursor()
table1=cur.execute("CREATE TABLE IF NOT EXISTS T1(ID INT)")
ins1=cur.execute("INSERT INTO T1(ID) VALUES(?)",(78,))
sel2=cur.execute("INSERT INTO T1(ID) VALUES(?)",(24,))
id1=31
id2=24
up1=cur.execute(f"UPDATE T1 SET ID={id1} WHERE ID={id2}")
alter1=cur.execute(f"ALTER TABLE T1 RENAME TO T2")
sel1=cur.execute("SELECT * FROM T2 WHERE ID<=?",(78,))
val1=sel1.fetchall()
for i in val1:
    print(i[0])'''
import calendar
print(calendar.calendar(2012))
print(2006-2012)