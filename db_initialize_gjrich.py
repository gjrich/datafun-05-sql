import sqlite3
import pathlib
import pandas as pd

# Your code here....
# Define paths...
# Define functions...

# Define the main function that will call your functions
def main():
    paths_to_verify = [sql_file_path, author_data_path, book_data_path]
    verify_and_create_folders(paths_to_verify)
    
    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, author_data_path, book_data_path)