-- Use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

-- Perform an INNER JOIN between Books and Author to retrieve book titles along with author names
SELECT Books.title, Author.first_name, Author.last_name
FROM Books
INNER JOIN Author ON Books.author_id = Author.author_id;