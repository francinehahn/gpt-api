"""Current Datetime"""
from datetime import datetime

def current_time():
    """Function that returns the current datetime in the format 2023-07-29 14:29:49"""
    datetime_now = datetime.now()
    datetime_format = "%Y-%m-%d %H:%M:%S"
    datetime_edited = datetime_now.strftime(datetime_format)
    return datetime_edited