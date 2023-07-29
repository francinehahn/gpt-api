"""index file"""
from api.app import app
from api.routes.UserRoutes import user_blueprint
from api.routes.RecipeRoutes import recipe_blueprint
from api.routes.TextRoutes import text_blueprint
from api.routes.TranslatorRoutes import translator_blueprint
from api.routes.SummaryRoutes import summary_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(recipe_blueprint)
app.register_blueprint(text_blueprint)
app.register_blueprint(translator_blueprint)
app.register_blueprint(summary_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
