from flask import Flask
from endpoints.summary import bp as bp_summary
from endpoints.writing_assistant import bp as bp_writing_assistant
from endpoints.translator import bp as bp_translator
from endpoints.create_recipe import bp as bp_create_recipe

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


app.register_blueprint(bp_summary)
app.register_blueprint(bp_writing_assistant)
app.register_blueprint(bp_translator)
app.register_blueprint(bp_create_recipe)


if __name__ == "__main__":
    app.run()
