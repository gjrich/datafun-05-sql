-- Use WHERE to filter data based on conditions
-- Find all books published after 1950
SELECT * FROM Books
WHERE year_published > 1950;

-- Find authors with the last name 'Orwell'
SELECT * FROM Author
WHERE last_name = 'Orwell';