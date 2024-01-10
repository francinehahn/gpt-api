"""Translator database"""
import os
from botocore.exceptions import ClientError
import boto3
from dotenv import load_dotenv

load_dotenv()

class TranslatorDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""
    def __init__(self):
        # dybmodb client
        dynamodb_client = boto3.resource(
            'dynamodb',
            aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
            aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
            region_name='sa-east-1'
        )
        self.table_translator = dynamodb_client.Table('translator_gpt')
        
    def create_translation(self, data):
        """This method receives the translation from the service layer and inserts it into the database"""
        try:
            self.table_translator.put_item(
                Item={
                    'id': data['translator_id'],
                    'question': data['text'],
                    'answer': data['answer'],
                    'user_id': data['user_id'],
                    'created_at': data['created_at']
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def get_translations(self, user_id):
        """This method receives a user_id and returns all the translations from the account"""
        try:
            translations = self.table_translator.scan(
                FilterExpression='user_id = :val',
                ExpressionAttributeValues={':val': user_id}
            )
            return translations
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def get_translation_by_id(self, translation_id):
        """This method receives a user_id and a translation_id and returns the translation"""
        try:
            translation = self.table_translator.get_item(
                Key={
                    'id': translation_id
                }
            )
            return translation
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def delete_translation_by_id(self, translation_id):
        """This method receives a user_id and a translation_id and deletes the translation"""
        try:
            self.table_translator.delete_item(
                Key={
                    'id': translation_id
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def regenerate_translation(self, data):
        """This method receives a user_id, a translation_id, and a new answer and updates the translation (answer)"""
        try:
            self.table_translator.update_item(
                Key={
                    'id': data['translation_id']
                },
                UpdateExpression='SET answer = :update',
                ExpressionAttributeValues={
                    ':update': data['answer']
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
            