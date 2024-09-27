# This script is part of the Module 5 project
# it is created to run various sql statements 
# These run on the tables in project.db
# The tables were created from the /data/*.csvs
# gjrich - Sept 2024


# import packages
import pathlib
import sqlite3
import logging

import pandas as pd


# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')


# Set root db path
db_filepath = pathlib.Path("project.db")



'''Implement SQL statements and queries to perform additional operations 
and use Python to execute your SQL statements. 
You might create an additional table, insert new records, 
and perform data querying (with filters, sorting, and joining tables), 
data aggregation, and record update and deletion.
Use Python to interact with the SQL database and execute SQL commands. 
'''

# Call the various Sql scripts from /sql/*.sql

def py_sql_insert(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")





# Logging

'''Logging is recommended for most professional projects. Implement logging to enhance debugging and maintain a record of program execution.

    Configure logging to write to a file named log.txt.
    Log the start of the program using logging.info().
    Log the end of the program using logging.info().
    Log exceptions using logging.exception().
    Log other major events using logging.info().
    Log the start and end of major functions using logging.debug().
'''


# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    ...
    logging.info("Program started") # add this at the beginning of the main method

    # Create database schema and populate with data
    # ... your code here to perform all required operations

    logging.info("All SQL operations completed successfully")
    
    logging.info("Program ended")  # add this at the end of the main method




# Conditionally execute the main() function if this is the script being run
if __name__ == "__main__":
    main()