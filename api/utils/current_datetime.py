"""Current Datetime"""
from datetime import datetime, timedelta

def current_time():
    """Function that returns the datetime in the format 2023-07-29 14:29:49 
    (3 hours less than the current time to be added to the database correctly)"""
    datetime_now = datetime.now() - timedelta(hours=3)
    datetime_format = "%Y-%m-%d %H:%M:%S"
    datetime_edited = datetime_now.strftime(datetime_format)
    return datetime_edited
