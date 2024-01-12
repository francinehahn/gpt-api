"""Translator service"""
import uuid
from botocore.exceptions import ClientError
from marshmallow import ValidationError
from api.schema.TranslatorSchema import TranslatorSchema
from api.schema.RegenerateTranslationSchema import RegenerateTranslationSchema
from api.errors.TranslatorErrors import TranslationNotFound
from api.errors.TranslatorErrors import NoTranslationsToUpdate
from api.utils.current_datetime import current_time

class TranslatorService:
    """This class receives data from the controller and returns the response from the open ai api"""
    def __init__(self, translator_database, authentication, open_ai):
        self.translator_database = translator_database
        self.authentication = authentication
        self.open_ai = open_ai
         
    def create_translation(self, data):
        """This method receives a source language, a target language and a text and returns the translation"""
        try:
            TranslatorSchema().load(data)
            user_id = self.authentication.get_identity()
            translator_id = str(uuid.uuid4())
            created_at = current_time()
            
            response = self.open_ai.generate_translation(data)
            print(response)
            data_db = {
                'translator_id': translator_id,
                'created_at': created_at,
                'user_id': user_id,
                'question': data['text'],
                'answer': response
            }
            self.translator_database.create_translation(data_db)
            return response
        except ValidationError as err:
            raise err
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
    
    def get_translations(self):
        """This method receives a token and sends the user_id to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            translations = self.translator_database.get_translations(user_id)

            response = []
            for translation in translations['Items']:
                response.append({
                    "id": translation[0],
                    "question": translation[1],
                    "answer": translation[2],
                    "user_id": translation[3],
                    "created_at": translation[4]
                })
            return response
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
        
    def delete_translation_by_id(self, translation_id):
        """This method receives a translation_id and a token and sends the info to the database layer"""
        try:
            user_id = self.authentication.get_identity()
            translation = self.translator_database.get_translation_by_id(user_id)
            
            if 'Item' not in translation:
                raise TranslationNotFound("Translation not found.")

            self.translator_database.delete_translation_by_id(translation_id)
        except TranslationNotFound as err:
            raise err
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
    
    def regenerate_translation(self, data):
        """This method receives a a token and sends the info to the database layer"""
        try:
            RegenerateTranslationSchema().load(data)
            user_id = self.authentication.get_identity()
            
            all_translations = self.translator_database.get_translations(user_id)
            if 'Items' in all_translations and len(all_translations['Items']) == 0:
                raise NoTranslationsToUpdate("There are no translations registered in the database.")

            all_translations = all_translations['Items']
            last_translation = all_translations[-1]
            translation_id = last_translation[0]

            formatted_translation = {
                "text": last_translation[1],
                "source_language": data['source_language'],
                "target_language": data['target_language']
            }

            response = self.open_ai.generate_translation(formatted_translation)
            self.translator_database.regenerate_translation({'translation_id': translation_id, 'answer': response})  
        except ValidationError as err:
            raise err
        except NoTranslationsToUpdate as err:
            raise err
        except ClientError as e:
            raise ClientError(str(e), 'DynamoDB Client Error.') from e
        