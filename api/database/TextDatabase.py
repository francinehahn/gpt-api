"""Text database"""
import os
from botocore.exceptions import ClientError
import boto3
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class TextDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""
    def __init__(self):
        # dybmodb client
        dynamodb_client = boto3.resource(
            'dynamodb',
            aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
            aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
            region_name='sa-east-1'
        )
        self.table_text = dynamodb_client.Table('writing_assistant_gpt')
    
    def create_text(self, data):
        """This method receives the text from the service layer and inserts it into the database"""
        try:
            self.table_text.put_item(
                Item={
                    'id': data['writing_assistant_id'],
                    'question': data['text'],
                    'answer': data['answer'],
                    'user_id': data['user_id'],
                    'created_at': data['created_at']
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def get_texts(self, user_id):
        """This method receives a user_id and returns all the texts from the account"""
        try:
            texts = self.table_text.scan(
                FilterExpression='user_id = :val',
                ExpressionAttributeValues={':val': user_id}
            )
            return texts
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def get_text_by_id(self, text_id):
        """This method receives a user_id and a text_id and returns the text"""
        try:
            text = self.table_text.get_item(
                Key={
                    'id': text_id
                }
            )
            return text
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def delete_text_by_id(self, text_id):
        """This method receives a user_id and a text_id and deletes the text"""
        try:
            self.table_text.delete_item(
                Key={
                    'id': text_id
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def regenerate_text(self, data):
        """This method receives a user_id, a text_id, and a new answer and updates the text (answer)"""
        try:
            self.table_text.update_item(
                Key={
                    'id': data['text_id']
                },
                UpdateExpression='SET answer = :update',
                ExpressionAttributeValues={
                    ':update': data['answer']
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
            