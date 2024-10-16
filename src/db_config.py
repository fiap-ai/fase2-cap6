import os
import cx_Oracle
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the Oracle Instant Client directory
oracle_client_path = os.getenv('ORACLE_CLIENT_PATH')
cx_Oracle.init_oracle_client(lib_dir=oracle_client_path)

# Database connection details
DB_CONFIG = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'dsn': os.getenv('DB_DSN')
}
