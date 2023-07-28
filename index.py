"""index file with all the endpoints"""
from api.app import app
from api.routes.user_routes import user_blueprint
from api.routes.gpt_routes import gpt_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(gpt_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
