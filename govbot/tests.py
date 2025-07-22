import unittest
from govbot import initialize_bot, get_response, MIN_CONFIDENCE

class TestGovbot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initialized, cls.bot = initialize_bot()

    def test_00_initialized(self):
        self.assertTrue(self.initialized)

    def _test_respostas(self, mensagens, palavras_chave_esperadas):
        for msg in mensagens:
            print(f"Testando: {msg}")
            resposta, confianca = get_response(self.bot, msg)
            self.assertGreaterEqual(confianca, MIN_CONFIDENCE)
            for palavra in palavras_chave_esperadas:
                self.assertIn(palavra.lower(), resposta.lower())

    def test_01_saudacoes(self):
        mensagens = [
            "oi", "olá", "fala govbot",
            "bom dia", "bom dia govbot", "govbot, bom dia",
            "boa tarde", "boa tarde, pode me ajudar?", "gov, boa tarde",
            "boa noite", "govbot, boa noite", "boa noite, me ajuda?"
        ]
        self._test_respostas(mensagens, ["govbot"])

    def test_02_acesso_govbr(self):
        mensagens = [
            "como acessar o portal gov.br?", "govbr como entro", "gov.br login"
        ]
        self._test_respostas(mensagens, ["gov.br"])

    def test_03_servicos_govbr(self):
        mensagens = [
            "o que posso fazer no gov.br?", "quais serviços estão no gov.br?", "gov.br tem o que?"
        ]
        self._test_respostas(mensagens, ["gov.br", "serviços"])

    def test_04_custos_govbr(self):
        mensagens = [
            "os serviços do gov.br são pagos?", "gov.br cobra alguma coisa?", "gov.br é gratuito?"
        ]
        self._test_respostas(mensagens, ["gov.br", "gratuitos"])

    def test_05_ajuda_govbr(self):
        mensagens = [
            "preciso de ajuda com o gov.br", "esqueci a senha do gov.br", "gov.br recuperar conta"
        ]
        self._test_respostas(mensagens, ["gov.br", "ajuda"])

    def test_06_seguro_desemprego(self):
        mensagens = [
            "como solicitar seguro desemprego no gov.br?", "entrar com pedido de seguro-desemprego", "como faço pra pegar seguro?"
        ]
        self._test_respostas(mensagens, ["seguro", "gov.br"])

    def test_07_rg(self):
        mensagens = [
            "como tirar RG?", "onde faço meu RG?", "quero fazer minha identidade"
        ]
        self._test_respostas(mensagens, ["identidade"])

    def test_08_cpf(self):
        mensagens = [
            "segunda via cpf", "como recuperar o CPF?", "emitir segunda via do CPF"
        ]
        self._test_respostas(mensagens, ["cpf", "segunda via"])

    def test_09_alistamento_militar(self):
        mensagens = [
            "alistamento militar documentos", "como me alisto no exército?", "onde me alisto?"
        ]
        self._test_respostas(mensagens, ["alistamento", "militar"])


if __name__ == "__main__":
    unittest.main()
