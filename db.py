import os
import psycopg2
from dotenv import load_dotenv

def get_connect():
    return psycopg2.connect(
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
    )
