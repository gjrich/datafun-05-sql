-- Use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

-- Perform an INNER JOIN between books and author to retrieve book titles along with author names
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.author_id;