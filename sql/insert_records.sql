-- insert at least 10 additional records into each table.
INSERT INTO books (book_id, title, year_published, author_id) VALUES
('0c5e72f4-3a71-4bdb-97cb-21c48fdfb9ed', 'One Hundred Years of Solitude', 1967, '07d53d7a-ec5f-4d5b-b8a2-f4eae02996ed'),
('b8536242-3e7b-4690-8a74-6f37c8bb2c38', 'Catch-22', 1961, '5d8e4a6c-65b7-4626-8d91-0b4db2407e9c'),
('f3bd62e4-2a82-495f-b0ae-45634b4acbdd', 'The Bell Jar', 1963, 'e6e3d3e9-60af-4394-a071-9355d7b2a7c9'),
('db47b837-df2e-46cb-92e9-c3e780b6bb5d', 'Emma', 1815, '69f825d4-7a7d-4329-a5f1-7432d242e8bb'),
('79941a59-2d4e-4e87-8b22-b88c0f5d4b70', 'Vanity Fair', 1848, 'e4c3e765-9125-4b95-bb71-13b95c51c7a1'),
('9f3a4511-81df-46c4-9a6f-d3b6ac4fcb89', 'The Stranger', 1942, '0efb7dc4-0df2-45ac-b569-5ebd7b42e187'),
('b2cd52cc-20e7-426b-84b4-0c77d8e7d14b', 'Lolita', 1955, 'ae8b76f0-957a-469a-bcb1-4e495b17eaf1'),
('f4dc61bc-eecf-4a94-90cb-108307d5d83c', 'The Road', 2006, '15bdbb6c-9496-4c1e-a2d5-4d0cfef93142'),
('7fa3e6df-8c62-41a6-8bfa-68e3b5560f7e', 'Slaughterhouse-Five', 1969, 'ce403fa1-d775-4f30-8c9f-30baf908db4d'),
('15e34bdf-fc9d-4b99-8a61-53e78447aeeb', 'The Color Purple', 1982, '75894079-148d-4920-873d-802566e3e002');

-- Insert corresponding records into the author table
INSERT INTO authors (author_id, last_name, first_name) VALUES
('07d53d7a-ec5f-4d5b-b8a2-f4eae02996ed', 'Garcia Marquez', 'Gabriel'),
('5d8e4a6c-65b7-4626-8d91-0b4db2407e9c', 'Heller', 'Joseph'),
('e6e3d3e9-60af-4394-a071-9355d7b2a7c9', 'Plath', 'Sylvia'),
('69f825d4-7a7d-4329-a5f1-7432d242e8bb', 'Austen', 'Jane'),
('e4c3e765-9125-4b95-bb71-13b95c51c7a1', 'Thackeray', 'William'),
('0efb7dc4-0df2-45ac-b569-5ebd7b42e187', 'Camus', 'Albert'),
('ae8b76f0-957a-469a-bcb1-4e495b17eaf1', 'Nabokov', 'Vladimir'),
('15bdbb6c-9496-4c1e-a2d5-4d0cfef93142', 'McCarthy', 'Cormac'),
('ce403fa1-d775-4f30-8c9f-30baf908db4d', 'Vonnegut', 'Kurt'),
('75894079-148d-4920-873d-802566e3e002', 'Walker', 'Alice');