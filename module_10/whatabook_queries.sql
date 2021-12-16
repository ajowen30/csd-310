/*
    Title: whatabook.init.sql
    Author: Avery Owen
    Date: 7 December 2021
    Description: WhatABook database initialization.
*/

-- Select query to view user wishlist
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book on wishlist.book_id = book.book_id
WHERE user.user_id = 1;

-- select query to view store location
SELECT store_id, locale from store;

-- Select query to view all books
SELECT book_id, book_name, author, details from book;

-- select query to view books not in wishlist
SELECT book_id, book_name, author, details 
FROM book;
WHERE book_id NOT IN(SELECT book_id FROM wishlist WHERE user_id = 1);

-- add new book to users wishlist
INSERT INTO wishlist(user_id, book_id)
    VALUES(1, 9)

-- remove book from users wishlist
DELETE FROM wishlist WHERE user_id = 1 AND book_id = 9;