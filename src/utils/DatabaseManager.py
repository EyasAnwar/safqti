import os
import psycopg
import itertools
from psycopg import Error


class DatabaseManager:
    _instance = None

    def __init__(self):
        self.connection = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
        return cls._instance

    def connect(self):
        try:
            self.connection = psycopg.connect(
                dbname=os.environ.get('DATABASE_NAME'),
                user=os.environ.get('DATABASE_USERNAME'),
                password=os.environ.get('DATABASE_PASSWORD'),
                host=os.environ.get('DATABASE_HOST'),
                port=os.environ.get('DATABASE_PORT'))
            print("Connected to the PostgreSQL database successfully.")
        except (Exception, Error) as e:
            print(f"Error connecting to the PostgreSQL database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the PostgreSQL database.")

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
            results = []
            try:
                results = cursor.fetchall()
                desc = cursor.description
                column_names = [col[0] for col in desc]

                results = [dict(itertools.zip_longest(column_names, row))
                           for row in results]
            except (Exception, Error) as e:
                pass
            return results
        except (Exception, Error) as e:
            print(f"Error executing query: {e}")

    def insert_record(self, table_name, record_data):
        columns = ', '.join(record_data.keys())
        placeholders = ', '.join(['%s'] * len(record_data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
        params = tuple(record_data.values())
        self.execute_query(query, params)

    def get_records(self, table_name):
        query = f"SELECT * FROM {table_name};"
        return self.execute_query(query)
