# Python3 and Sqlite3

* Insert row into table

* Database table name: `todoApp`

* createTodoApp.sh

```
DROP TABLE todoApp;
    CREATE TABLE todoApp(
     id INTEGER PRIMARY KEY AUTOINCREMENT, 
     key_item TEXT NOT NULL,
     todo_item TEXT NOT NULL
 );
 
INSERT INTO todoApp(key_item, todo_item) VALUES('key2', 'Buy milk today 2');
```

* Shell command to create table in `sqlite3`

```
sqlite3 test_sqlite3.db < createTodoApp.sh
```

