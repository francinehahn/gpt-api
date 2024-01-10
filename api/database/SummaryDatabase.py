"""Summary database"""
import os
from botocore.exceptions import ClientError
import boto3
from dotenv import load_dotenv

load_dotenv()

class SummaryDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""
    def __init__(self):
        # dybmodb client
        dynamodb_client = boto3.resource(
            'dynamodb',
            aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
            aws_access_key_id=os.getenv("ACCESS_KEY_ID"),
            region_name='sa-east-1'
        )
        self.table_summary = dynamodb_client.Table('summary_gpt')

    def create_summary(self, data):
        """This method receives the summary from the service layer and inserts it into the database"""
        try:
            self.table_summary.put_item(
                Item={
                    'id': data['summary_id'],
                    'question': data['text'],
                    'answer': data['answer'],
                    'user_id': data['user_id'],
                    'created_at': data['created_at']
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def get_summaries(self, user_id):
        """This method receives a user_id and returns all the summaries from the account"""
        try:
            summaries = self.table_summary.scan(
                FilterExpression='user_id = :val',
                ExpressionAttributeValues={':val': user_id}
            )
            return summaries
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def get_summary_by_id(self, summary_id):
        """This method receives a user_id and a summary_id and returns the summary"""
        try:
            summary = self.table_summary.get_item(
                Key={
                    'id': summary_id
                }
            )
            return summary
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def delete_summary_by_id(self, summary_id):
        """This method receives a user_id and a summary_id and deletes the summary"""
        try:
            self.table_summary.delete_item(
                Key={
                    'id': summary_id
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e

    def regenerate_summary(self, data):
        """This method receives a user_id, a summary_id, and a new answer and updates the summary (answer)"""
        try:
            self.table_summary.update_item(
                Key={
                    'id': data['summary_id']
                },
                UpdateExpression='SET answer = :update',
                ExpressionAttributeValues={
                    ':update': data['answer']
                }
            )
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
            