#!/usr/local/bin/python3.11

import sqlite3

# Sun Jun  2 01:01:47 2024 
# KEY: sqlite3, insert table, database
#
# NOTE: insert row with autoincrement primary key
#
#
# createTodoApp.sh
#
# sqlite3 test_sqlite3.db < createTodoApp.sh
#
#
# DROP TABLE todoApp;
# CREATE TABLE todoApp(
#     id INTEGER PRIMARY KEY AUTOINCREMENT, 
#     key_item TEXT NOT NULL,
#     todo_item TEXT NOT NULL
# );
# 
# INSERT INTO todoApp(key_item, todo_item) VALUES('key2', 'Buy milk today 2');
#

mydb = '/Users/aaa/myfile/bitbucket/database/test_sqlite3.db'
con = sqlite3.connect(mydb)
cur = con.cursor()
res = cur.execute("SELECT * FROM todoApp")
print(res.fetchone())

cur.execute('''
  INSERT INTO todoApp (key_item, todo_item) VALUES(?,?)
  ''', ('key5', 'item5'))

con.commit();

cur.execute('select * from todoApp')
users = cur.fetchall()
for row in users:
  print(row)

