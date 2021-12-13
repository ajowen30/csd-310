""" 
    Title: what_a_book.py
    Author: Avery Owen
    Date: 8 December 2021
    Description: Console program for whatabook program
"""

""" import statements """
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


def show_menu():
    """ Show Menu to user and then ask them to enter their choice to view. Return their input, or exit if their input is invalid """


    print("-----Main Menu-----")

    print("     1. View Books\n     2. View Store Locations\n       3. My Account\n     4. Exit")

    try:
        choice = int(input("\nPress: \n1 to view books\n 2 to view store locations\n 3 to view my account\n 4 to exit"))

        return choice
    except ValueError:
        print("\n Error! Invalid number.")

        sys.exit(0)


def show_books(_cursor):
    """ Executing the cursor to select the chosen columns from the book table """
    _cursor.execute("\nSELECT book_id, book_name, author, details from book")

    books = _cursor.fetchall()

    print("\n-----Displaying Book Listing-----")

    """ Displays all book names, authors, and details within the book table"""
    for book in books:
        print(" Book Name: {}\n Author{}\n  Details{}\n".format(book[0], book[1], book[2]))


def show_locations(_cursor):
    """ Executing the cursor to select the chosen columns from the store table """
    _cursor.execute("\n SELECT store_id, local from store")

    locations - _cursor.fetchall()

    print("\n-----Displaying Store Locations-----")

    """ Displays all locations from store table"""
    for location in locations:
        print("  Locale: {}\n".format(location[1]))


def validate_user():
    """ Ask user for a user id"""
    try:
        user_id = int(input("Please enter a customer id: "))
        
        """Exit program if the user id is less than 0 or greater than 3"""
        if user_id < 0 or user_id > 3:
            print("\nError! Invalid customer number.")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n Error! Please enter a valid number.")
        sys.exit(0)


def show_account_menu():
    """ Print account menu. Ask user to choose which option from the menu they would like to look at. Error and exit if input is not a valid number"""

    try:
        print("\n --- Customer Menu ---")
        print(" 1. Wishlist\n 2. Add Book\n 3. Main Menu")

        account_option = int(input("\nPress: \n1 to view Wishlist\n 2 to add a book\n 3 to go back to the main menu"))

        return account_option
    except ValueError:
        print("Error! Please enter a valid number.")
        sys.exit(0)


def show_wishlist(_cursor, _user_id):
    """ two Inner joins are needed to display the users wishlist, combining user and book tables"""

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    show_wishlist = _cursor.fetchall()

    print("\n --- Displaying Wishlist Items ---")

    for books in wishlist:
        print(" Book Name: {}\n Author: {}\n".format(book[4], book[5]))


def show_books_to_add(_cursor, _user_id):
    """ Query database for books not already in the users wishlist """

    query = ("SELECT book_id, book_name, author, details " 
                "FROM book " 
                "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n --- Displaying Available Books ---")

    for book in books_to_add:
        print(" Book Id: {}\n Book Name: {}\n".format(book[0], book[1]))


def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))


try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the WhatABook database 

    cursor = db.cursor() 

    print("\n  Welcome to the WhatABook Application! ")

    user_selection = show_menu() # show main menu 


    while user_selection != 4:

        # user selects option 1, call show_books method and display books
        if user_selection == 1:
            show_books(cursor)

        #user selects option 2, call show_locations method and display locations
        if user_selection == 2:
            show_locations(cursor)

        #user selects option 3, call validate_user method to validate the entered user_id 
        # call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the use selects option 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # commit the changes to the database 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")

                # show the account menu 
                account_option = show_account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please retry...")
            
        # show the main menu
        user_selection = show_menu()

    print("\n\n  Program terminated...")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()