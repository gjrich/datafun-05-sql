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

# Set file path of each SQL statement
# could include in function name but that looks gross
# it also is easily duplicated if we add additional .sql files in the future

# create_tables_path=pathlib.Path("sql").joinpath("create_tables.sql")
insert_records_path=pathlib.Path("sql").joinpath("insert_records.sql")
update_records_path = pathlib.Path("sql").joinpath("update_records.sql")
delete_records_path = pathlib.Path("sql").joinpath("delete_records.sql")
query_aggregation_path = pathlib.Path("sql").joinpath("query_aggregation.sql")
query_filter_path = pathlib.Path("sql").joinpath("query_filter.sql")
query_sorting_path = pathlib.Path("sql").joinpath("query_sorting.sql")
query_group_by_path = pathlib.Path("sql").joinpath("query_group_by.sql")
query_join_path = pathlib.Path("sql").joinpath("query_join.sql")


# Call the various Sql scripts from /sql/*.sql

'''def py_sql_create_tables(db_filepath, create_tables_path):
    with sqlite3.connect(db_filepath) as conn:
        with open(create_tables_path, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {create_tables_path}")'''

def py_sql_insert_records(db_filepath, insert_records_path):
    with sqlite3.connect(db_filepath) as conn:
        with open(insert_records_path, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {insert_records_path}")



def py_sql_update_records(db_filepath, update_records_path):
    with sqlite3.connect(db_filepath) as conn:
        with open(update_records_path, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {update_records_path}")

def py_sql_delete_records(db_filepath, delete_records_path):
    with sqlite3.connect(db_filepath) as conn:
        with open(delete_records_path, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {delete_records_path}")

def py_sql_query_aggregation(db_filepath, query_aggregation_path):
    with sqlite3.connect(db_filepath) as conn:
        with open(query_aggregation_path, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_aggregation_path}")

def py_sql_query_filter(db_filepath, query_filter_path):
    with sqlite3.connect(db_filepath) as conn:
        with open(query_filter_path, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_filter_path}")

def py_sql_query_sorting(db_filepath, query_sorting_path):
    with sqlite3.connect(db_filepath) as conn:
        with open(query_sorting_path, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_sorting_path}")

def py_sql_query_group_by(db_filepath, query_group_by_path):
    with sqlite3.connect(db_filepath) as conn:
        with open(query_group_by_path, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_group_by_path}")

def py_sql_query_join(db_filepath, query_join_path):
    with sqlite3.connect(db_filepath) as conn:
        with open(query_join_path, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_join_path}")



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
    logging.info("Program started")

    # Create database schema and populate with data
   # py_sql_create_tables(db_filepath, create_tables_path)
    #logging.info("Running create_tables.sql")
    
    py_sql_insert_records(db_filepath, insert_records_path)
    logging.info("Running insert_records.sql")

    py_sql_update_records(db_filepath, update_records_path)
    logging.info("Running update_records.sql")

    py_sql_delete_records(db_filepath, delete_records_path)
    logging.info("Running delete_records.sql")

    py_sql_query_aggregation(db_filepath, query_aggregation_path)
    logging.info("Running query_aggregation.sql")

    py_sql_query_filter(db_filepath, query_filter_path)
    logging.info("Running query_filter.sql")

    py_sql_query_sorting(db_filepath, query_sorting_path)
    logging.info("Running query_sorting.sql")

    py_sql_query_group_by(db_filepath, query_group_by_path)
    logging.info("Running query_group_by.sql")

    py_sql_query_join(db_filepath, query_join_path)
    logging.info("Running query_join.sql")
        

    logging.info("All SQL operations completed successfully")
    
    logging.info("Program ended")  # add this at the end of the main method




# Conditionally execute the main() function if this is the script being run
if __name__ == "__main__":
    main()