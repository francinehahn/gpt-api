from flask import jsonify, request

class GptController:
    """This class receives data from the HTTP request and returns the response"""

    def __init__(self, gpt_service):
        self.gpt_service = gpt_service

    def create_recipe(self):
        try:
            data = request.json
            response = self.gpt_service().create_recipe(data)
            
            response = jsonify(
                message = "Aqui está a receita:",
                data = response,
            )
            
            response.status_code = 201
            return response
        
        except Exception as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def create_summary(self):
        try:
            data = request.json
            response = self.gpt_service().create_summary(data)
            
            response = jsonify(
                message = "Aqui está o resumo do texto:",
                data = response
            )
            
            response.status_code = 201
            return response
        
        except Exception as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def translator(self):
        try:
            data = request.json
            response = self.gpt_service().translator(data)

            response = jsonify(
                message = "Aqui está a tradução que você pediu:",
                data = response
            )
            response.status_code = 201
            return response
    
        except Exception as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        
    def writing_assistant(self):
        try:
            data = request.json
            response = self.gpt_service().writing_assistant(data)

            response = jsonify(
                message = "Aqui está o texto que você pediu:",
                data = response
            )
            response.status_code = 201
            return response
    
        except Exception as err:
            response = jsonify(
                message = f"Unexpected error: {err}"
            )
            response.status_code = 400
            return response
        