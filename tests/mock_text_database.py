"""Mock Text Database"""
class MockTextDatabase:
    """This class receives data from the service layer and inserts the answer from the openAI api into the database"""

    def create_text(self, writing_assistant_id, text, answer, user_id, created_at):
        """This method receives the text from the service layer and inserts it into the database"""

    def get_texts(self, user_id):
        return {
            "texts": [
                {
                    "answer": " e sua importância\n\nA Torre Eiffel é uma das mais famosas construções do mundo, não é à toa que ela é um dos monumentos mais visitados de Paris. Ela foi projetada por Gustave Eiffel e foi inaugurada em 1889 como parte das comemorações do centenário da Revolução Francesa.\n\nA Torre Eiffel é muito mais do que apenas uma atração turística: ela simboliza o orgulho de todos os franceses. Ela é um símbolo de força e de perseverança, além de representar a ousadia e o pioneirismo da França.\n\nAlém disso, a torre Eiffel é um ícone cultural importante na história da humanidade. Durante a Segunda Guerra Mundial, ela foi a primeira a ser visível quando os Aliados libertaram Paris.\n\nA Torre Eiffel é um símbolo global de esperança, de resistência e de romantismo. A sua presença tem encantado turistas de todos os cantos do mundo desde 1889, e a ela é uma grande responsável pelo encanto que Paris gera em seus visitantes.",
                    "created_at": "Sat, 29 Jul 2023 14:56:19 GMT",
                    "id": "b595899a-c7bb-4231-88d3-fe75890bd826",
                    "question": "A torre Eiffel",
                    "user_id": "8a85573b-2ea2-43a4-9c8d-91b959e6da3c"
                },
                {
                    "answer": "\n\nA linhaça é conhecida por ser uma excelente fonte de diversos nutrientes e benefícios para a saúde. Ela é rica em ômega 3, fibras e ferro, fornecendo muitos benefícios para o coração, a saúde digestiva, a saúde da pele e muito mais.\n\nA linhaça é uma grande fonte de ácidos graxos ômega 3, que ajudam a reduzir a inflamação, melhorar o funcionamento do sistema imunológico, reduzir a pressão arterial e ajudar a reduzir o colesterol.\n\nA linhaça também é rica em fibras solúveis, que ajudam a absorver água, aumentam a sensação de saciedade e ajudam a regular o funcionamento do intestino, o que é útil no tratamento e prevenção de diarréia e constipação.\n\nAlém disso, a linhaça também é uma boa fonte de ferro, o que ajuda a reduzir o risco de anemia. O ferro é essencial para a produção de glóbulos vermelhos saudáveis e para o transporte de oxigênio no corpo.\n\nA linhaça também tem antioxidantes, que ajudam a combater os radicais livres que são prejudiciais à saúde e ajudam na prevenção de doenças crônicas. Além disso, os antioxidantes também ajudam na prevenção do envelhecimento precoce.\n\nPortanto, a linhaça é uma excelente fonte de nutrientes e benefícios para a saúde. Comer linhaça regularmente pode ajudar a melhorar a saúde geral, prevenir doenças e melhorar a qualidade de vida.",
                    "created_at": "Sat, 29 Jul 2023 16:10:42 GMT",
                    "id": "f91f267a-3e59-497b-91e8-7dbb395c9b83",
                    "question": "Benefícios da linhaça",
                    "user_id": "8a85573b-2ea2-43a4-9c8d-91b959e6da3c"
                }
            ]
        }

    def get_text_by_id(self, user_id, text_id):
        """This method receives a user_id and a text_id and returns the text"""
        return ('04bace90-ce1f-46f1-8fc5-96f9c19024f5', 'Raças de cachorro mais populares no mundo', '\n\nOs cachorros são, sem dúvida, um dos animais mais populares do mundo. Existem muitas raças de cachorro diferentes de todos os tamanhos e tipos, tornando difícil escolher a melhor para você. Por isso, separamos aqui as 10 raças de cachorro mais populares no mundo.\n\n1. Border Collie – Este cão de trabalho inteligente e ativo é um dos queridinhos dos donos por seu caráter leal, energético e obediência.\n\n2. Labrador Retriever – Esta raça é uma das mais populares por seu caráter dócil, sua versatilidade e seu amor incondicional por toda família.\n\n3. Golden Retriever – Seu temperamento calmo, fácil de treinar e amorosa faz desta raça uma das mais leais e adoradas.\n\n4. Pastoral Alemão – Esta raça de cão tem uma personalidade de guarda e proteção, além de ser carinhoso e adorável.\n\n5. Bulldog Francês – Este cão de raça pequena é um companheiro leal e dócil.\n\n6. Beagle – Versátil e inteligente, este cão é ideal para qualquer tipo de família.\n\n7. Pug – Esta raça tem uma personalidade encantadora e adora brincar.\n\n8. ShihTzu – Esta raça tem uma natureza dócil e carinhosa que torna o cachorro extremamente amoroso.\n\n9. Bulldog Inglês – Seu temperamento calmo e amoroso torna esta raça um ótimo companheiro.\n\n10. Pastor Australiano – Esta raça adora estar constantemente perto da família, além de ser muito inteligente e obediente.\n\nSe você está buscando uma raça para fazer parte da sua família, essas 10 raças de cachorro são excelentes opções. Escolha a que mais se adequa ao seu estilo de vida e se divirta com seu novo melhor amigo!', '8a85573b-2ea2-43a4-9c8d-91b959e6da3c', 'datetime.datetime(2023, 7, 29, 17, 24, 16)')

    def delete_text_by_id(self, user_id, text_id):
        """This method receives a user_id and a text_id and deletes the text"""
        
    def regenerate_text(self, answer, user_id, text_id):
        """This method receives a user_id, a text_id, and a new answer and updates the text (answer)"""