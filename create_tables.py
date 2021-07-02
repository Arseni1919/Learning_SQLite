import sqlite3
from sqlite3 import Error
from create_db import create_connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def main():
    connection = create_connection("app_db.sqlite")
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
    create_posts_table = """
    CREATE TABLE IF NOT EXISTS posts(
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      title TEXT NOT NULL, 
      description TEXT NOT NULL, 
      user_id INTEGER NOT NULL, 
      FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """
    execute_query(connection, create_posts_table)

    create_comments_table = """
    CREATE TABLE IF NOT EXISTS comments (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      text TEXT NOT NULL, 
      user_id INTEGER NOT NULL, 
      post_id INTEGER NOT NULL, 
      FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
    );
    """

    create_likes_table = """
    CREATE TABLE IF NOT EXISTS likes (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      user_id INTEGER NOT NULL, 
      post_id integer NOT NULL, 
      FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
    );
    """

    execute_query(connection, create_comments_table)
    execute_query(connection, create_likes_table)




if __name__ == '__main__':
    main()