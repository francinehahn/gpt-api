"""Mock Translator Database"""
class TranslatorDatabaseMock:
    """This class is a mock of the translator database layer"""

    def create_translation(self, translator_id, text, answer, user_id, created_at):
        """This method receives the translation from the service layer and inserts it into the database"""

    def get_translations(self, user_id):
        """This method receives a user_id and returns all the translations from the account"""
        return [(
            "\n\nDogs are loved by many people around the world. There are many different breeds, but some stand out for being the most popular. Among the best known breeds are German Shepherd, Labrador Retriever, Golden Retriever, Bulldog, Beagle, Yorkshire Terrier, Boxer, Cocker Spaniel, Chihuahua and Poodle. The German Shepherd is known for its guard and work abilities, is loyal and very intelligent. The Labrador Retriever is considered the most popular pet dog in the world. The Golden Retriever is known for its friendly personality and unconditional love. The Bulldog is loyal, brave and very friendly. The Beagle is cheerful, playful and active. The Yorkshire Terrier is small, intelligent and very brave. The Boxer is strong, brave and affectionate. The Cocker Spaniel is friendly, affectionate and very active. The Chihuahua is a very intelligent and brave pet dog. The Poodle is elegant, intelligent and friendly. These popular dog breeds are known for being great companions and loyal to their owners. If you are thinking of adopting a dog, these breeds are excellent options.",
            "Sat, 29 Jul 2023 17:23:53 GMT",
            "06f065e3-59d3-4c0b-8a6d-3e7f3d885316",
            "Os cachorros são amados por muitas pessoas ao redor do mundo. Existem muitas raças diferentes, mas algumas se destacam por serem as mais populares. Dentre as raças mais conhecidas estão o Pastor Alemão, o Labrador Retriever, o Golden Retriever, o Bulldog, o Beagle, o Yorkshire Terrier, o Boxer, o Cocker Spaniel, o Chihuahua e o Poodle. O Pastor Alemão é conhecido por suas habilidades de guarda e trabalho, é leal e muito inteligente. O Labrador Retriever é considerado o cão de companhia mais popular do mundo. O Golden Retriever é conhecido por sua personalidade amigável e amor incondicional. O Bulldog é leal, corajoso e muito amigável. O Beagle é alegre, brincalhão e ativo. O Yorkshire Terrier é pequeno, inteligente e muito destemido. O Boxer é forte, corajoso e carinhoso. O Cocker Spaniel é amigável, carinhoso e muito ativo. O Chihuahua é um cão de companhia muito inteligente e corajoso. O Poodle é elegante, inteligente e amigável.Estas raças de cachorro populares são conhecidas por serem ótimas para companhia e leais a seus donos. Se você estiver pensando em adotar um cachorro, estas raças são excelentes opções.",
            "8a85573b-2ea2-43a4-9c8d-91b959e6da3c"
        )]
    
    def get_translation_by_id(self, user_id, translation_id):
        """This method receives a user_id and a translation_id and returns the translation"""
        if translation_id == "incorrect_id":
            return None
        else:
            return ('cb012510-fc3f-4c38-86fd-f43943cb5bf4', 'Bélgica é uma nação da Europa Ocidental, formada por celtas, franceses e alemães. Possui clima temperado e vegetação característicos. A Bélgica foi um importante centro comercial ao longo da história, sendo atualmente uma das nações mais desenvolvidas e industrializadas do mundo, com uma economia voltada para o setor terciário. É governada por uma monarquia constitucional e possui uma moderna infraestrutura de transportes, bem como políticas progressistas de Direitos Humanos.', '\n\nالبلجيك هي دولة في غرب أوروبا، تتكون من الإيطاليين، الفرنسيين والألمان. لديها مناخ معتدل ونباتات ذات شخصيّة. كانت البلجيك أحد المراكز التجارية اللأهم في التاريخ، وهي الآن واحدة من الدول الأكثر تطوراً وتصنيعاً في العالم، وتعتمد على اقتصاد القطاع الثالث. وتتحكم بالنظام الدستوري المل لكي، وتتمتع ببنية تحتية وسائل النقل الحديثة، كما تحتوي على سياسات تقدمية لحقوق الإنسان.', '8a85573b-2ea2-43a4-9c8d-91b959e6da3c', 'datetime.datetime(2023, 7, 29, 17, 23, 53)')

    def delete_translation_by_id(self, user_id, translation_id):
        """This method receives a user_id and a translation_id and deletes the translation"""

    def regenerate_translation(self, answer, user_id, translation_id):
        """This method receives a user_id, a translation_id, and a new answer and updates the translation (answer)"""