import os
import mariadb
from dotenv import load_dotenv

# 1. Load variables from the .env file
load_dotenv()

def get_connection():
    # 2. Create and return a MariaDB connection
    return mariadb.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3333")),
        user=os.getenv("DB_USER", "happyuser"),
        password=os.getenv("DB_PASSWORD", "happypassword"),
        database=os.getenv("DB_NAME", "happy_paws"),
    )
