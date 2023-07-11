from flask import jsonify, request, Blueprint
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

bp = Blueprint('translator', __name__)

@bp.route("/translator", methods=["POST"])
def translator():
    try:
        body = request.json

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Traduza o seguinte texto do {body['source_language']} para o {body['target_language']}: {body['text']}",
            temperature=0.8,
            max_tokens=2048,
            n=1,
            stop=None
        )

        response = jsonify(
            message = "Aqui está a tradução que você pediu:",
            data = response['choices'][0]['text']
        )
        response.status_code = 201
        return response
    
    except Exception as err:
        response = jsonify(
            message = f"Unexpected error: {err}"
        )
        response.status_code = 400
        return response