"""
Sqlite database connection and initialization
This module provides a class for connecting to an SQLite database and executing SQL queries.
"""

import sqlite3
from app.database.base import BaseDatabase

class SQLiteDatabase(BaseDatabase):
    """
    SQLite database implementation of BaseDatabase.
    """

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.set_schema()

    def connect(self):
        """
        Connect to the SQLite database.
        """
        self.connection = sqlite3.connect(self.db_path)

    def disconnect(self):
        """
        Disconnect from the SQLite database.
        """
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query: str):
        """
        Execute a query on the SQLite database.

        :param query: SQL query to execute

        :return: Result of the query execution
        """
        if not self.connection:
            raise ConnectionError("Database is not connected.")
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        return cursor.fetchall()
    
    def get_cursor(self):
        """
        Get a cursor for the SQLite database.

        :return: SQLite cursor
        """
        if not self.connection:
            raise ConnectionError("Database is not connected.")
        return self.connection.cursor()

    def set_schema(self):
        """
        Set the database schema.
        """
        with open("app/database/schema.sql", "r") as file:
            schema = file.read()

        self.execute_query(schema)

    