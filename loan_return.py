import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()
from datetime import date


def loan_return():
    isbn = input("Enter the book isbn to return: ")
    isbn = int(isbn)
    return_date = date.today()
    loaned = 0

    with conn:
        c.execute("""UPDATE loans SET loaned=?, return_date=? WHERE isbn=?""",
                  (loaned, return_date, isbn, ))

        conn.commit()
        print(c.rowcount)
        if c.rowcount > 0:
            print("Book returned, isbn {}".format(isbn))


if __name__ == '__main__':
    loan_return()