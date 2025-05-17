from abc import ABC, abstractmethod


class BaseDatabase(ABC):
    """
    Abstract base class for database operations.
    """

    @abstractmethod
    def connect(self):
        """
        Connect to the database.
        """
        pass

    @abstractmethod
    def disconnect(self):
        """
        Disconnect from the database.
        """
        pass

    @abstractmethod
    def execute_query(self, query: str):
        """
        Execute a query on the database.

        :param query: SQL query to execute

        :return: Result of the query execution
        """

    def set_schema(self):
        """
        Set the database schema.
        """
        pass

    