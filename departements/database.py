import mysql.connector as mysql

def connexion_db():
    return mysql.connect(
        user='root',
        password= 'MariaDB',
        host='localhost',
        database='agence'
        )