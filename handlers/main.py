import repository

from lambda_decorators import json_http_resp

connection = repository.create_connection()


@json_http_resp
def handler(event, context):
    user_id = event["user_id"]
    username = repository.get_user_name(connection, user_id)

    if username is None:
        raise Exception("User does not exist")

    return {"username": username}
