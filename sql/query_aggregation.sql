-- Use aggregation functions including COUNT, AVG, SUM
-- Count the number of books in the Books table
SELECT COUNT(*) AS total_books FROM books;

-- Calculate the average year of publication for books
SELECT AVG(year_published) AS average_year FROM books;

-- Sum of all publication years
SELECT SUM(year_published) AS total_years FROM books;