from abc import ABC, abstractmethod

class DatabaseInterface(ABC):

    @abstractmethod
    def read(self, query, params=None):
        pass

    @abstractmethod
    def stream_read(self, query, params=None):
        pass

    @abstractmethod
    def insert(self, table, columns, values):
        pass

    @abstractmethod
    def bulk_upsert(self, table, columns, values_list, key_columns):
        pass

    @abstractmethod
    def update(self, table, set_clause, where_clause, params):
        pass

    @abstractmethod
    def execute(self, query, params=None):
        pass

    @abstractmethod
    def close(self):
        pass
