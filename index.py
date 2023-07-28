"""index file"""
from api.app import app
from api.routes.UserRoutes import user_blueprint
from api.routes.GptRoutes import gpt_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(gpt_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
