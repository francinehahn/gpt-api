from flask import Flask
from endpoints.summary import bp as bp_summary


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


app.register_blueprint(bp_summary)


if __name__ == "__main__":
    app.run()
