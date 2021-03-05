import psycopg2
import os


def create_connection():
    user_name = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')
    host = os.getenv('DB_HOST', 'localhost')
    port = 5432

    return psycopg2.connect(
        user=user_name,
        password=password,
        host=host,
        port=port,
        database=database
    )


def get_user_name(connection, user_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM users WHERE id = %s", (user_id,))

        result = cursor.fetchone()

        if result is not None:
            return str(result[0])
        return None


def create_user(connection, id, name):
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO users VALUES (%s, %s)', (id, name))
    connection.commit()


def destroy_all(connection):
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM users')
    connection.commit()
