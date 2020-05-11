import sqlite3


DATABASE = 'E:/python_workspace/chat_2_flask/app/main/model/users.db'


def connect_db():
    return sqlite3.connect(DATABASE)
