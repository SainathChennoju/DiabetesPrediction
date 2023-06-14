import sqlite3

conn=sqlite3.connect('patient.db')

cur=conn.cursor()
#cur.execute('create table patients patient_id int,patient_name varchar(30)')
#cur.execute("insert into patients values(2,'sai')")
#cur.execute("insert into patients values(2,'hari','no_diabetes')")
#cur.execute("create table patientinfo(name varchar(30),result varchar(20))")
cur.execute("insert into patientinfo values('arun','no_diabetes')")
conn.commit()