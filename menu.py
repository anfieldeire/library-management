from loan_request import loan_request
from loan_check import book_check
from loan_return import loan_return
from users_add import add_user
from users_update import update_user


def selection_validate():

    valid_selections = ('1', '2', '3', '4')
    message = input("Welcome to the main menu. Press enter to continue: ")
    loop = 'yes'
    while True and loop == 'yes':

        selection = input("\nPlease select from the following menu (Type exit to exit program) \n"
                          "To request a new loan enter 1 \n"
                          "To return a book enter 2 \n"
                          "To add a user enter 3 \n"
                          "To update a user enter 4 \n"
                          "Enter choice: ")
        if selection == 'exit':
            break
        else:
            if selection in valid_selections:
                print("{}".format(selection))
                loop = 'no'

            else:
                print('\nValue: {} did not match any menu choice'.format(selection))
                loop = 'yes'
    return selection


def selection_calls():

    selection = selection_validate()

    print("Selection made was : {} ".format(selection))

    if selection == '1':
        book_check()

    elif selection == 2:
        loan_return()

    elif selection == 3:
        add_user()

    elif selection == '4':
        print("update user")
        update_user()


if __name__ == '__main__':
   selection_calls()