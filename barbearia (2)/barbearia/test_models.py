# test_models.py

# Testes unitários da classe Agendamento (models.py).

# Aqui testamos apenas a lógica da classe (POO), sem depender de
# conexão com o banco de dados — por isso são "testes unitários":
# cada teste verifica uma unidade isolada de comportamento.

import unittest
from models import Agendamento


class TestAgendamento(unittest.TestCase):

    def setUp(self):
        """Executado antes de cada teste: cria um agendamento de exemplo."""
        self.agendamento = Agendamento(
            cliente="João Silva",
            telefone="(47) 99999-0000",
            servico="Corte de cabelo",
            preco=35.0,
            barbeiro="Carlos",
            data="2026-09-20",
            horario="09:00",
            status="Agendado",
            id=1
        )

    def test_criacao_atributos(self):
        """Verifica se os atributos são atribuídos corretamente no construtor."""
        self.assertEqual(self.agendamento.cliente, "João Silva")
        self.assertEqual(self.agendamento.barbeiro, "Carlos")
        self.assertEqual(self.agendamento.status, "Agendado")
        self.assertEqual(self.agendamento.preco, 35.0)

    def test_status_padrao(self):
        """Verifica se o status assume 'Agendado' quando não é informado."""
        agendamento_sem_status = Agendamento(
            cliente="Maria",
            telefone="123456",
            servico="Barba",
            preco=20.0,
            barbeiro="André",
            data="2026-09-21",
            horario="10:00"
        )
        self.assertEqual(agendamento_sem_status.status, "Agendado")

    def test_exibir_contem_dados_principais(self):
        """Verifica se exibir() retorna uma string com os principais dados."""
        texto = self.agendamento.exibir()
        self.assertIn("João Silva", texto)
        self.assertIn("Carlos", texto)
        self.assertIn("Agendado", texto)
        self.assertIsInstance(texto, str)

    def test_converte_tupla(self):
        """Verifica se converte_tupla() gera a tupla no formato esperado (sem o id)."""
        tupla = self.agendamento.converte_tupla()
        esperado = (
            "João Silva", "(47) 99999-0000", "Corte de cabelo", 35.0,
            "Carlos", "2026-09-20", "09:00", "Agendado"
        )
        self.assertEqual(tupla, esperado)
        self.assertEqual(len(tupla), 8)

    def test_reverte_tupla(self):
        """Verifica se reverte_tupla() reconstrói corretamente um objeto Agendamento."""
        tupla_do_banco = (
            5, "Pedro Souza", "(47) 98888-1111", "Barba", 25.0,
            "Marcos", "2026-09-22", "14:00", "Concluído"
        )
        agendamento = Agendamento.reverte_tupla(tupla_do_banco)

        self.assertIsInstance(agendamento, Agendamento)
        self.assertEqual(agendamento.id, 5)
        self.assertEqual(agendamento.cliente, "Pedro Souza")
        self.assertEqual(agendamento.status, "Concluído")
        self.assertEqual(agendamento.preco, 25.0)

    def test_reverte_tupla_eh_staticmethod(self):
        """Verifica que reverte_tupla pode ser chamado sem instanciar a classe."""
        tupla_do_banco = (
            1, "Teste", "0000", "Serviço", 10.0, "Barbeiro",
            "2026-09-23", "08:00", "Agendado"
        )
        # Chamado diretamente pela classe, sem criar um objeto antes
        resultado = Agendamento.reverte_tupla(tupla_do_banco)
        self.assertEqual(resultado.cliente, "Teste")


if __name__ == "__main__":
    unittest.main()
