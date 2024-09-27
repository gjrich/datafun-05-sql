-- Use GROUP BY clause (and optionally with aggregation)
-- Group books by the author and count how many books each author has
SELECT author_id, COUNT(*) AS book_count
FROM books
GROUP BY author_id;