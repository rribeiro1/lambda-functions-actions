import repository

connection = repository.create_connection()


def create_user(id, name):
    repository.create_user(connection, id, name)


def reset_database():
    repository.destroy_all(connection)

