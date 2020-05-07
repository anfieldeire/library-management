import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()
from datetime import timedelta, date


def loan_add( ):

    isbn = int(input("Please enter the book isbn to be loaned: "))
    library_id = int(input("Please enter the user id of the loanee: "))

    loan_date = date.today()
    print("Today's date is: {}".format(loan_date))
    due_date = loan_date + timedelta(days=14)
    print("Return date is: {}".format(due_date))

    with conn:
        book_found = c.execute("SELECT * from books WHERE isbn=:isbn",
                               {'isbn': isbn})
        book_found = c.fetchone()
        if book_found:

            c.execute(""" INSERT into loans ( library_id, loaned, loan_date, isbn, due_date) VALUES
                    (?, ?, ?, ?, ? )""", (library_id, 1, loan_date, isbn, due_date ))

            conn.commit()
            return c.lastrowid

loan_add()


def loan_return_date():

    today = date.today()
    print("Today's date is: {}".format(today))
    return_date = today + timedelta(days=14)
    print("Return date is: {}".format(return_date))

    return today, return_date

#loan_return_date()