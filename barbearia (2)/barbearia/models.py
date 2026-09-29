# models.py
# Classe que representa um agendamento da barbearia

class Agendamento:
    def __init__(self, cliente, telefone, servico, preco, barbeiro,
                 data, horario, status="Agendado", id=None):
        self.id = id
        self.cliente = cliente
        self.telefone = telefone
        self.servico = servico
        self.preco = preco
        self.barbeiro = barbeiro
        self.data = data
        self.horario = horario
        self.status = status

    def exibir(self):
        """Retorna os dados do agendamento formatados em uma única linha."""
        return (f"[{self.id}] {self.cliente} | {self.servico} | "
                f"R$ {self.preco:.2f} | {self.barbeiro} | "
                f"{self.data} {self.horario} | {self.status}")

    def converte_tupla(self):
        """Converte o objeto Agendamento em uma tupla (útil para INSERT/UPDATE)."""
        return (self.cliente, self.telefone, self.servico, self.preco,
                self.barbeiro, self.data, self.horario, self.status)

    @staticmethod
    def reverte_tupla(tupla):

        return Agendamento(
            id=tupla[0],
            cliente=tupla[1],
            telefone=tupla[2],
            servico=tupla[3],
            preco=tupla[4],
            barbeiro=tupla[5],
            data=tupla[6],
            horario=tupla[7],
            status=tupla[8]
        )
    def __repr__(self):
        return self.exibir()
