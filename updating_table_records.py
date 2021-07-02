import sqlite3
from sqlite3 import Error
from create_db import create_connection
from selecting_records import execute_read_query
from inserting_records import execute_query


def main():
    connection = create_connection("app_db.sqlite")
    select_post_description = "SELECT description FROM posts WHERE id = 2"
    post_description = execute_read_query(connection, select_post_description)
    for description in post_description:
        print(description)

    update_post_description = """
    UPDATE
      posts
    SET
      description = "The weather has become pleasant now"
    WHERE
      id = 2
    """
    execute_query(connection, update_post_description)


if __name__ == '__main__':
    main()