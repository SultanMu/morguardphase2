import psycopg2
from datetime import datetime

class CompanyDatabaseHandler:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    def connect(self):
        """Establish a connection to the PostgreSQL database."""
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            raise

    def close_connection(self):
        """Close the connection to the PostgreSQL database."""
        if self.connection:
            self.connection.close()

    def insert_data(self, files_data):
        """Insert multiple records into the API_company table."""
        try:
            if self.connection is None:
                self.connect()

            with self.connection.cursor() as cursor:
                for data in files_data:
                    insert_query = """
                        INSERT INTO API_company 
                        (type, title, created_date, next_asses_date, company, author, summary, file_name, flag, date_processed)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                 
                    values = (
                        data['type'],
                        data['title'],
                        data['created_date'],
                        data['next_asses_date'],
                        data['company'],
                        data['author'],
                        data['summary'],
                        data['file_name'],
                        data['flag'],
                        datetime.now().date()  
                    )
                    cursor.execute(insert_query, values)
          
                self.connection.commit()

        except Exception as e:
            print(f"An error occurred during the insert operation: {e}")
            if self.connection:
                self.connection.rollback()  
            raise
