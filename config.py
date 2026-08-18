import mysql.connector as m

def connect():

    conn = m.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306
    )

    cur = conn.cursor()

    cur.execute("CREATE DATABASE IF NOT EXISTS testpy")

    conn.close()

    conn = m.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="testpy"
    )

    print("PYTHON MYSQL CONNECTION IS READY !!!!!")

    return conn