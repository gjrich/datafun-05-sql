-- Update the row in the Author table, keeping the author_id the same
UPDATE Author
SET last_name = 'Orwell', first_name = 'George'
WHERE author_id = '10f88232-1ae7-4d88-a6a2-dfcebb22a596';

-- Update the row in the Books table, keeping the book_id and author_id the same
UPDATE Books
SET title = 'Animal Farm', year_published = 1945
WHERE book_id = 'd6f83870-ff21-4a5d-90ab-26a49ab6ed12' 
  AND author_id = '10f88232-1ae7-4d88-a6a2-dfcebb22a596';