import psycopg2
from datetime import datetime
import sys
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)  # Logs will also be output to console
    ]
)
logger = logging.getLogger(__name__)
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
            logger.error(f"Error connecting to the database: {e}")
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
                logger.info(f"Insertion Successful")

        except Exception as e:
            logger.error(f"An error occurred during the insert operation: {e}")
            if self.connection:
                self.connection.rollback()  
            raise
