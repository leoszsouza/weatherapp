import unittest

from main import *


class TestBuscaHistorico(unittest.TestCase):


    def test_busca_historico(self):
        """
            Teste que valida se foi realizada a busca do histórico
        """
        data = buscahistorico()
        self.assertIsNotNone(data)

    def test_insere_historico(self):
        """
            Teste que valida se foi realizada a inclusão da busca na tabela de histórico
        """
        inserirhistorico('91910')
        data = buscahistorico();
        self.assertIsNotNone(data)

    def test_busca_temperatura(self):
        """
            Teste que valida se foi realizada a busca da temperatura
        """
        data = query_api('91910')
        self.assertIsNotNone(data)


if __name__ == '__main__':
    unittest.main()