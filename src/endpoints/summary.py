from flask import jsonify, request, Blueprint
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

bp = Blueprint('summary', __name__)

@bp.route("/summary", methods=["POST"])
def summary():
    body = request.json

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Resuma o seguinte texto: {body['text']}",
        temperature=0.8,
        max_tokens=2048,
        n=1,
        stop=None
    )

    response = jsonify(
        message = "Here is the summary of the text:",
        data = response['choices'][0]['text']
    )
    response.status_code = 201
    return response
