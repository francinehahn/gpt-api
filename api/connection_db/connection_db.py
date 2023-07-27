import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

config = {
    "host":  os.getenv("host"),
    "user": os.getenv("user"),
    "password": os.getenv("password"),
    "database": os.getenv("database")
}