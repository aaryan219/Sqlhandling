from sqlachemy import create_engine, text
import pandas as pd

class UniversalSQLHandler:
    def __init__(self, db_type, host, port, db_name, username, password, driver=None):
        db_type = db_type.lower()

        if db_type == 'postgresql':
            driver = driver or 'psycopg2'
            self.connection_url = f"postgresql+{driver}://{username}:{password}@{host}:{port}/{db_name}"

        elif db_type == 'mysql':
            driver = driver or 'pymysql'
            self.connection_url = f"mysql+{driver}://{username}:{password}@{host}:{port}/{db_name}"

        elif db_type in ['mssql', 'sqlserver']:
            driver = driver or 'pyodbc'
            self.connection_url = (
                f"mssql+{driver}://{username}:{password}@{host}:{port}/{db_name}"
                "?driver=ODBC+Driver+17+for+SQL+Server"
            )
        else:
            raise ValueError(f"Unsupported DB type: {db_type}")

        self.engine = create_engine(self.connection_url)
        self.connection = self.engine.connect()

    def read(self, query, params=None):
        return pd.read_sql(text(query), self.connection, params=params)

    def stream_read(self, query, params=None):
        result = self.connection.execution_options(stream_results=True).execute(text(query), params or {})
        for row in result:
            yield dict(row)

    def insert(self, table, columns, values):
        placeholders = ', '.join([f":{col}" for col in columns])
        cols = ', '.join(columns)
        query = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
        self.connection.execute(text(query), dict(zip(columns, values)))

    def bulk_upsert(self, table, columns, values_list, key_columns):
        for values in values_list:
            key_values = {k: values[columns.index(k)] for k in key_columns}
            existing = self.read(
                f"SELECT 1 FROM {table} WHERE " + " AND ".join([f"{k} = :{k}" for k in key_columns]),
                key_values
            )
            if existing.empty:
                self.insert(table, columns, values)
            else:
                set_cols = [col for col in columns if col not in key_columns]
                set_clause = ', '.join([f"{col} = :{col}" for col in set_cols])
                where_clause = ' AND '.join([f"{k} = :{k}" for k in key_columns])
                update_dict = {col: values[columns.index(col)] for col in columns}
                query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
                self.connection.execute(text(query), update_dict)

    def update(self, table, set_clause, where_clause, params):
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        self.connection.execute(text(query), params)

    def execute(self, query, params=None):
        self.connection.execute(text(query), params or {})

    def close(self):
        self.connection.close()
        self.engine.dispose()
