/*
    Title: whatabook.init.sql
    Author: Avery Owen
    Date: 7 December 2021
    Description: WhatABook database initialization.
*/

DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant all privileges
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;


-- Create tables
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);


--insert store record 
INSERT INTO store(locale)
    VALUES('1234 Rainbow Road');

--insert book records 
INSERT INTO book(book_name, author, details)
    VALUES('Philosopher Stone', 'J.K Rowling', 'First Book in the Harry Potter Series');

INSERT INTO book(book_name, author, details)
    VALUES('Chamber of Secrets', 'J.K Rowling', 'Second Book in the Harry Potter Series');

INSERT INTO book(book_name, author, details)
    VALUES('Prisonser of Azkaban', 'J.K Rowling', 'Third Book in the Harry Potter Series');

INSERT INTO book(book_name, author, details)
    VALUES('Goblet of Fire', 'J.K Rowling', 'Fourth Book in the Harry Potter Series');

INSERT INTO book(book_name, author, details)
    VALUES('Order of the Phoenix', 'J.K Rowling', 'Fifth Book in the Harry Potter Series');

INSERT INTO book(book_name, author, details)
    VALUES('Half-Blood Prince', 'J.K Rowling', 'Sixth Book in the Harry Potter Series');

INSERT INTO book(book_name, author, details)
    VALUES('Deathly Hallows', 'J.K Rowling', 'Seventh Book in the Harry Potter Series');

INSERT INTO book(book_name, author, details)
    VALUES('Fear and Loathing in Las Vegas', 'Hunter S. Thompson', 'A savage journey to the heart of the American Dream');

INSERT INTO book(book_name, author, details)
    VALUES('Cats Cradle', 'Kurt Vonnegut', 'Satirical postmodern novel');

-- insert user
INSERT INTO user(first_name, last_name) 
    VALUES('Avery', 'Owen');

INSERT INTO user(first_name, last_name)
    VALUES('Joe', 'Smith');

INSERT INTO user(first_name, last_name)
    VALUES('John', 'Doe');

-- insert wishlist records 
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Avery'), 
        (SELECT book_id FROM book WHERE book_name = 'Fear and Loathing in Las Vegas')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Joe'),
        (SELECT book_id FROM book WHERE book_name = 'Cats Cradle')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'),
        (SELECT book_id FROM book WHERE book_name = 'Deathly Hallows')
    );