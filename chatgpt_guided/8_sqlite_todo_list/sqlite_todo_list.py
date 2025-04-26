"""
SQLite Todo App – Command-line app to add, list, and delete tasks using sqlite3.
"""

import sqlite3

try:
    with sqlite3.connect("todo_list.db") as conn:
        print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

except sqlite3.OperationalError as e:
    print("Failed to open database:", e)


"""
This one was done a little differently... The task suggestino was not specific, so basically I create a sqlite database with python (which is not necessary). The creation of tables, adding items, listing and deleting are handled from the command line. I was not too concerned about this feature as I have created plenty of websites that have a more sophisticated database interface.

sqlite> create table todo_list (id integer primary key autoincrement, name text);
sqlite> insert into todo_list (name) values ("go shopping");
sqlite> insert into todo_list (name) values ("wash car");
sqlite> select * from todo_list;
sqlite> delete from todo_list where id = 2;
sqlite> select * from todo_list;
"""