"Recipe Database Mock"
class RecipeDatabaseMock:
    """This is a mock of the recipe database layer"""

    def create_recipe(self, recipe_id, ingredients, answer, user_id, created_at):
        """This method receives the recipe from the service layer and inserts it into the database"""
        print(recipe_id, ingredients, answer, user_id, created_at)
    
    def get_recipes(self, user_id):
        """This method receives a user_id and returns all the recipes from the account"""
        return [('bc00d081-cd87-4e1f-8a84-3b1fc676a3ad', 'arroz arbóreo, queijo, cogumelos, cebola, alho, maracujá', '\n\nRisoto de Maracujá com Queijo\n\nIngredientes:\n\n- 1 xícara de arroz arbóreo\n- 2 colheres de sopa de azeite\n- 1/2 cebola picada\n- 2 dentes de alho picado\n- 2 xícaras de cogumelos fatiados\n- 2 xícaras de caldo de legumes\n- 1/2 xícara de suco de maracujá\n- 1/2 xícara de queijo ralado\n- Sal e pimenta a gosto\n- 1/4 xícara de salsinha fresca picada\n\nInstruções:\n\n1. Em uma panela grande, aqueça o azeite em fogo médio. Adicione a cebola e o alho e refogue por cerca de 3 minutos, mexendo até ficar macio.\n\n2. Adicione o arroz arbóreo e os cogumelos e cozinhe por mais 2 minutos, até que o arroz comece a dourar.\n\n3. Acrescente o caldo de legumes, o suco de maracujá e tempere com sal e pimenta a gosto. Reduza o fogo para baixo e tampe a panela. Cozinhe por cerca de 18-20 minutos, mexendo de vez em quando, até que o arroz esteja cozido.\n\n4. Retire do fogo e adicione o queijo ralado e a salsinha. Misture bem e sirva.', '8a85573b-2ea2-43a4-9c8d-91b959e6da3c', 'datetime.datetime(2023, 7, 29, 14, 36, 4)')]
    
    def get_recipe_by_id(self, user_id, recipe_id):
        """This method receives a user_id and a recipe_id and returns the recipe"""
        if recipe_id == "incorrect_id":
            return None
        else:
            return ('c77e265a-2fcc-4f04-bc75-3970dd00c9c0', 'leite, açúcar, manteiga, chocolate em pó, essência de baunilha, leite condensado, paçoca', '\n\nReceita de Brownie com Paçoca\n\nIngredientes:\n\n- 1 xícara (chá) de leite\n- 1 xícara (chá) de açúcar\n- ½ xícara (chá) de manteiga\n- 3 colheres (sopa) de chocolate em pó\n- 1 colher (sopa) de essência de baunilha\n- ½ lata de leite condensado\n- 6 unidades de paçoca\n\nModo de Preparo:\n\n1. Derreta a manteiga em uma panela no fogo médio.\n\n2. Adicione o leite, o açúcar, o chocolate em pó e a essência de baunilha, mexendo bem para incorporar todos os ingredientes.\n\n3. Cozinhe por cerca de 5 minutos, mexendo sempre para não grudar.\n\n4. Desligue o fogo e acrescente o leite condensado, misturando bem.\n\n5. Em um refratário untado com manteiga, despeje a mistura e, por cima, espalhe as paçocas.\n\n6. Leve ao forno preaquecido em temperatura média por cerca de 25 minutos ou até dourar.\n\n7. Retire do forno e deixe esfriar antes de servir.', '8a85573b-2ea2-43a4-9c8d-91b959e6da3c', 'datetime.datetime(2023, 7, 29, 17, 29, 59)')

    def delete_recipe_by_id(self, user_id, recipe_id):
        """This method receives a user_id and a recipe_id and deletes the recipe"""

    def regenerate_recipe(self, answer, user_id, recipe_id):
        """This method receives a user_id, a recipe_id, and new answer and updates the recipe (answer)"""