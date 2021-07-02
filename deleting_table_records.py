import sqlite3
from sqlite3 import Error
from create_db import create_connection
from selecting_records import execute_read_query
from inserting_records import execute_query


def main():
    connection = create_connection("app_db.sqlite")
    delete_comment = "DELETE FROM comments WHERE id = 5"
    execute_query(connection, delete_comment)


if __name__ == '__main__':
    main()