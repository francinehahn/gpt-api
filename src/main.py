from flask import Flask
from endpoints.summary import bp as bp_summary
from endpoints.writing_assistant import bp as bp_writing_assistant

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


app.register_blueprint(bp_summary)
app.register_blueprint(bp_writing_assistant)


if __name__ == "__main__":
    app.run()
