from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_book(id, Comment,Year,Price):
    query = "INSERT INTO Gifts(ID,Comment,Year,Price) VALUES(%s,%s,%s,%s)"
    args = (id, Comment,Year,Price)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def main():
   insert_book(5, 'Hello', 1992, 1)

if __name__ == '__main__':
    main()