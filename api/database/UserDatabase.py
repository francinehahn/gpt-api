"""User database"""
import os
from botocore.exceptions import ClientError
import boto3
from api.errors.UserErrors import EmailAlreadyInUse
from dotenv import load_dotenv, find_dotenv

load_dotenv()

class UserDatabase:
    """Database layer"""
    def __init__(self):
        # dybmodb client
        dynamodb_client = boto3.resource(
            'dynamodb',
            aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
            aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
            region_name='sa-east-1'
        )
        self.table_users = dynamodb_client.Table('users_gpt')
        
    def create_user(self, user_id, data):
        """This method receives the user info from the service layer and inserts it into the database"""
        try:
            self.table_users.put_item(
                Item={
                    'id': user_id,
                    'user_name': data['user_name'],
                    'email': data['email'],
                    'phone': data['phone'],
                    'password': data['password']
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def get_user_by_email(self, email):
        """This method receives the user email from the service layer and returns the user info"""
        try:
            user = self.table_users.scan(
                FilterExpression='email = :val',
                ExpressionAttributeValues={':val': email}
            )
            return user
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
            