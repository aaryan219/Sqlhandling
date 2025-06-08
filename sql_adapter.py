from db_interface import DatabaseInterface
from universal_handler import UniversalSQLHandler

class SQLAdapter(DatabaseInterface):
    def __init__(self, db_type, host, port, db_name, username, password):
        self.handler = UniversalSQLHandler(db_type, host, port, db_name, username, password)

    def read(self, query, params=None):
        return self.handler.read(query, params)

    def stream_read(self, query, params=None):
        return self.handler.stream_read(query, params)

    def insert(self, table, columns, values):
        self.handler.insert(table, columns, values)

    def bulk_upsert(self, table, columns, values_list, key_columns):
        self.handler.bulk_upsert(table, columns, values_list, key_columns)

    def update(self, table, set_clause, where_clause, params):
        self.handler.update(table, set_clause, where_clause, params)

    def execute(self, query, params=None):
        self.handler.execute(query, params)

    def close(self):
        self.handler.close()
