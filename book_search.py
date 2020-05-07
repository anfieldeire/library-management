import sqlite3
from users_search import find_user
conn = sqlite3.connect('library.db')
c = conn.cursor()


def book_search():
    isbn = 4

    result_dict = {}
    with conn:
        book_found = c.execute("SELECT * from books WHERE isbn=:isbn",
                        {'isbn': isbn})
        book_found = c.fetchone()
        if book_found:
            # print("Book found: {}".format(book_found))
            # print(type(book_found))
            result_dict = {'Name': book_found[0], 'author': book_found[1], 'category': book_found[2], 'isbn': book_found[3]}
            print(c.rowcount)
            print(result_dict)
            return result_dict

        else:
            print("No results")

book_search()