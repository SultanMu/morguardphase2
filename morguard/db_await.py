import time
import psycopg2
from psycopg2 import OperationalError
import os

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=os.getenv("name"),
                user=os.getenv("user"),
                password=os.getenv("password"),
                host=os.getenv("host"),
                port=os.getenv("port")
            )
            conn.close()
            break
        except OperationalError:
            print("Database not ready, waiting...")
            time.sleep(5)

if __name__ == "__main__":
    wait_for_db()
    print("Database is up...")
