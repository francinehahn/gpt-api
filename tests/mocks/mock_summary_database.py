"""Mock Summary Database"""

class MockSummaryDatabase:
    """This is a mock of the summary database layer"""

    def create_summary(self, summary_id, text, answer, user_id, created_at):
        """This method receives the summary from the service layer and inserts it into the database"""
        
    def get_summaries(self, user_id):
        """This method receives a user_id and returns all the summaries from the account"""
        return [(
            "\n\nO dólar americano é uma das moedas mais importantes do mundo, sendo usado como referência em qualquer negócio em nível global. Apesar de sua hegemonia ser incontestável, ela é relativamente recente, pois só se deu após o fim da Segunda Guerra Mundial. Seu nome vem da palavra thaler, e sua adoção começou com a necessidade de financiar a Guerra da Independência dos Estados Unidos, em 1776. Até a metade do século XIX, a libra esterlina era a moeda de referência internacional. Não havia lei que desse ao Estado o controle exclusivo da emissão de moeda, o que propiciou a existência de inúmeras formas de pagamento. A unificação da moeda se deu somente em 1863 com o National Banking Act.",
            "Sat, 29 Jul 2023 15:00:14 GMT",
            "7dbffb0c-5cdd-4e65-b9aa-fee4f2f400f0",
            "O dólar americano é uma das moedas mais importantes no mundo. Atualmente, sua hegemonia é incontestável, já que é usada na adoção de reservas internacionais por Bancos Centrais de inúmeros países e como referência em qualquer negócio em nível global. Entretanto, nem sempre foi assim. Na verdade, a hegemonia da moeda norte-americana é relativamente recente, pois só se deu após o fim da Segunda Guerra Mundial. O dólar foi idealizado a partir da necessidade de criação de uma moeda que fosse capaz de financiar a Guerra da Independência dos Estados Unidos, em 1776, e fomentar a nova nação. Assim, em 1786 o Congresso Continental das já independentes 13 colônias aprovou o dólar como moeda nacional. O nome dollar vem da palavra thaler, uma conhecida moeda de prata que circulava na Europa durante o século XV. Todavia, até a metade do século XIX, período em que a libra esterlina tinha status de moeda internacional, os Estados Unidos eram considerados devedores de pouca credibilidade no cenário internacional e, ao contrário da maioria dos países europeus, não havia em sua Constituição nenhuma lei que desse ao Estado o controle exclusivo da emissão de moeda. Essa falta de legislação, inclusive, levou a uma situação caótica, pois propiciou a existência sem controle de inúmeras formas de pagamento. Para se ter uma ideia, qualquer indivíduo podia abrir um banco e emitir cédulas sem nenhuma autorização ou controle do governo. A primeira tentativa de unificação dos pagamentos partiu das necessidades de financiamento da Guerra de Secessão, em 1861. Desta forma, o governo passou a emitir notas que, baseadas em sua boa-fé e reputação, poderiam ser convertidas em ouro: as chamadas greenbacks, nome até hoje dado de forma informal ao dólar. A unificação da moeda como forma de pagamento se deu somente em 1863, com o National Banking Act.",
            "8a85573b-2ea2-43a4-9c8d-91b959e6da3c"
        )]
    
    def get_summary_by_id(self, user_id, summary_id):
        """This method receives a user_id and a summary_id and returns the summary"""
        if summary_id == "incorrect_id":
            return None
        else:
            return ('03187fc5-ad03-4356-89e0-441635c1b64b', 'A Bélgica é uma nação da Europa Ocidental internacionalmente conhecida como o centro da União Europeia. A formação do país foi resultante de povoações de celtas, franceses e alemães. O território belga é caracterizado pelo clima e vegetação tipicamente temperados. Ao longo da história, os belgas exerceram grande influência econômica mundial, com destaque para a tradição comercial local. Atualmente, a Bélgica é uma das nações mais desenvolvidas e industrializadas do mundo, com uma economia voltada para o setor terciário. O país é governado por uma monarquia constitucional e possui uma moderna infraestrutura de transportes. A sociedade civil e política belga é marcada pela adoção de políticas progressistas de Direitos Humanos.', '\n\nA Bélgica é uma nação da Europa Ocidental, formada por celtas, franceses e alemães. Possui clima temperado e vegetação característicos. A Bélgica foi um importante centro comercial ao longo da história, sendo atualmente uma das nações mais desenvolvidas e industrializadas do mundo, com uma economia voltada para o setor terciário. É governada por uma monarquia constitucional e possui uma moderna infraestrutura de transportes, bem como políticas progressistas de Direitos Humanos.', '8a85573b-2ea2-43a4-9c8d-91b959e6da3c', 'datetime.datetime(2023, 7, 29, 17, 23, 42)')

    def delete_summary_by_id(self, user_id, summary_id):
        """This method receives a user_id and a summary_id and deletes the summary"""

    def regenerate_summary(self, answer, user_id, summary_id):
        """This method receives a user_id, a summary_id, and a new answer and updates the summary (answer)"""