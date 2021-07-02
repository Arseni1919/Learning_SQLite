import sqlite3
from sqlite3 import Error
from create_db import create_connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def main():
    connection = create_connection("app_db.sqlite")

    # SELECT
    select_users = "SELECT * from users"
    users = execute_read_query(connection, select_users)

    for user in users:
        print(user)

    print()
    select_posts = "SELECT * FROM posts"
    posts = execute_read_query(connection, select_posts)

    for post in posts:
        print(post)

    print('join:')
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

    print(' multiple join:')
    # JOIN
    select_posts_comments_users = """
    SELECT
      posts.description as post,
      text as comment,
      name
    FROM
      posts
      INNER JOIN comments ON posts.id = comments.post_id
      INNER JOIN users ON users.id = comments.user_id
    """

    posts_comments_users = execute_read_query(
        connection, select_posts_comments_users
    )

    for posts_comments_user in posts_comments_users:
        print(posts_comments_user)

    print('column names')
    cursor = connection.cursor()
    cursor.execute(select_posts_comments_users)
    cursor.fetchall()

    column_names = [description[0] for description in cursor.description]
    print(column_names)

    print('WHERE:')
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


if __name__ == '__main__':
    main()