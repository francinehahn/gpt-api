"""Text service"""
import uuid
from mysql.connector import Error
from marshmallow import ValidationError
from api.schema.WritingAssistantSchema import WritingAssistantSchema
from api.errors.TextErrors import TextNotFound
from api.errors.TextErrors import NoTextsToUpdate
from api.utils.current_datetime import current_time

class TextService:
    """This class receives data from the controller and returns the response from the open ai api"""
    def __init__(self, text_database, authentication, open_ai):
        self.text_database = text_database
        self.authentication = authentication
        self.open_ai = open_ai

    def create_text(self, data):
        """This method receives a subject and returns the text"""
        try:
            WritingAssistantSchema().load(data)
            user_id = self.authentication.get_identity()
            writing_assistant_id = str(uuid.uuid4())
            created_at = current_time()

            response = self.open_ai.generate_text(data['text'])
            self.text_database.create_text(writing_assistant_id, data['text'], response, user_id, created_at)
            return response
        except ValidationError as err:
            raise err
        except Error as err:
            raise err
    
    def get_texts(self):
        """This method receives a token and sends the user_id to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            texts = self.text_database.get_texts(user_id)

            response = []
            for text in texts:
                response.append({
                    "id": text[0],
                    "question": text[1],
                    "answer": text[2],
                    "user_id": text[3],
                    "created_at": text[4]
                })
            return response
        except Error as err:
            raise err
        
    def delete_text_by_id(self, text_id):
        """This method receives a text_id and a token and sends the info to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            text = self.text_database.get_text_by_id(user_id, text_id)
            if text is None:
                raise TextNotFound("Text not found.")

            self.text_database.delete_text_by_id(user_id, text_id)
        except TextNotFound as err:
            raise err
        except Error as err:
            raise err
        
    def regenerate_text(self):
        """This method receives a a token and sends the info to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            all_texts = self.text_database.get_texts(user_id)
            if len(all_texts) == 0:
                raise NoTextsToUpdate("There are no texts registered in the database.")

            last_text = all_texts[-1]
            text_id = last_text[0]
            question = last_text[1]

            response = self.open_ai.generate_text(question)
            self.text_database.regenerate_text(response, user_id, text_id)
        except NoTextsToUpdate as err:
            raise err
        except Error as err:
            raise err
        