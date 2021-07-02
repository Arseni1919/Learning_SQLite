# Learning SQLite and `sqlite3`

## About

### SQLite

SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.

### `sqlite3`

The sqlite3 module was written by Gerhard Häring. It provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.


## Important Steps

### Create DB

```python
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("app_db.sqlite")
```

`connection = sqlite3.connect(path)` uses .connect() from the sqlite3 module and takes the SQLite database path as a parameter. If the database exists at the specified location, then a connection to the database is established. Otherwise, a new database is created at the specified location, and a connection is established.

### Creating Tables

```python
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      age INTEGER,
      name TEXT NOT NULL,
      gender TEXT,
      nationality TEXT
    );
    """
execute_query(connection, create_users_table)
```

### Inserting Records

```python
create_users = """
    INSERT INTO
      users (name, age, gender, nationality)
    VALUES
      ('James', 25, 'male', 'USA'),
      ('Leila', 32, 'female', 'France'),
      ('Brigitte', 35, 'female', 'England'),
      ('Mike', 40, 'male', 'Denmark'),
      ('Elizabeth', 21, 'female', 'Canada');
    """
    execute_query(connection, create_users)
```

### Selecting Records

To select records using SQLite, you can again use cursor.execute(). However, after you’ve done this, you’ll need to call .fetchall(). This method returns a list of tuples where each tuple is mapped to the corresponding row in the retrieved records.

To simplify the process, you can create a function `execute_read_query()`.

```python
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create_connection("app_db.sqlite")

# SELECT
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)

# JOIN
select_users_posts = """
SELECT
  users.id,
  users.name,
  posts.description
FROM
  posts
  INNER JOIN users ON users.id = posts.user_id
"""
users_posts = execute_read_query(connection, select_users_posts)
for users_post in users_posts:
    print(users_post)

# WHERE
select_post_likes = """
SELECT
  description as Post,
  COUNT(likes.id) as Likes
FROM
  likes,
  posts
WHERE
  posts.id = likes.post_id
GROUP BY
  likes.post_id
"""
post_likes = execute_read_query(connection, select_post_likes)
for post_like in post_likes:
    print(post_like)
```

By using a WHERE clause, you’re able to return more specific results.

To return column names, you can use the `.description` attribute of the `cursor` object. For instance, the following list returns all the column names for the above query:

```python
cursor = connection.cursor()
cursor.execute(select_posts_comments_users)
cursor.fetchall()

column_names = [description[0] for description in cursor.description]
print(column_names)
```

### Updating Table Records

```python
update_post_description = """
UPDATE
  posts
SET
  description = "The weather has become pleasant now"
WHERE
  id = 2
"""
execute_query(connection, update_post_description)
```

### Deleting Table Records

```python
delete_comment = "DELETE FROM comments WHERE id = 5"
execute_query(connection, delete_comment)
```

## Credits

- [Introduction to Python SQL Libraries - Real Python](https://realpython.com/python-sql-libraries/#understanding-the-database-schema)
- [Datatypes in sqlite3](https://www.sqlite.org/datatype3.html)
- [1 - SQLite tutorial - medium](https://medium.com/swlh/data-analysis-sqlite3-in-python-1868903eaee)
- [2 - SQLite tutorial - medium](https://medium.com/road-to-full-stack-data-science/create-and-manipulate-sqlite-tables-within-python-a-must-have-skill-for-data-scientists-3c12474fa050)
- [sqlite-commands](https://www.sqlitetutorial.net/sqlite-commands/)
- [Flask and SQLite](https://flask.palletsprojects.com/en/2.0.x/tutorial/database/)















