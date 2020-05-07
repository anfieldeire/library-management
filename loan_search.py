import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()

def loan_search():

    isbn = 1
    result_dict = {}
    with conn:
        loan_found = c.execute(" SELECT * from loans WHERE isbn = isbn ",
                            {'isbn': isbn})

        loan_found = c.fetchone()
        if loan_found:
            result_dict = {'isbn': loan_found[0], 'return_date': loan_found[1], 'library_id': loan_found[2],
            'loaned': loan_found[3], 'loan_date':loan_found[4]}
            print(result_dict)

        else:
            print("No exiting loans for isbn: {}".format(isbn))


loan_search()