from python_mysql_dbconfig import read_db_config
from mysql.connector import MySQLConnection, Error

def insert_books(books):
    query = "INSERT INTO Gifts VALUES(%s,%s,%s,%s)"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, books)

        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()

def main():
    books = [(6, 'Hello8', 1992, 1),
             (7, 'Hello9', 1995, 8),
             (8, 'Hello0', 1996, 6)]
    insert_books(books)

if __name__ == '__main__':
    main()