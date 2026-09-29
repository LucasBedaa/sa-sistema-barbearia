# agendamentos.py
# Camada de acesso a dados (DAO) da tabela "agendamentos".

import mysql.connector
from banco import conectar
from models import Agendamento


def listar_agendamentos():
    """
    Retorna uma lista de objetos Agendamento,
    ordenados por data e horário.
    """
    conexao = None
    cursor = None
    lista = []
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, cliente, telefone, servico, preco, barbeiro,
                   data, horario, status
            FROM agendamentos
            ORDER BY data, horario
        """)
        resultados = cursor.fetchall()
        lista = [Agendamento.reverte_tupla(linha) for linha in resultados]
    except mysql.connector.Error as erro:
        print(f"Erro ao listar agendamentos: {erro}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()
    return lista


def buscar_agendamento(id):
    """
    Retorna um objeto Agendamento correspondente ao id informado,
    ou None caso não seja encontrado.
    """
    conexao = None
    cursor = None
    agendamento = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, cliente, telefone, servico, preco, barbeiro,
                   data, horario, status
            FROM agendamentos
            WHERE id = %s
        """, (id,))
        resultado = cursor.fetchone()
        if resultado is not None:
            agendamento = Agendamento.reverte_tupla(resultado)
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar agendamento: {erro}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()
    return agendamento


def atualizar_status(id, novo_status):
    """
    Atualiza o status de um agendamento existente
    (ex.: para cancelar ou marcar como concluído).

    Retorna True se a atualização afetou alguma linha, False caso contrário
    (id inexistente ou erro de banco).
    """
    conexao = None
    cursor = None
    sucesso = False
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE agendamentos SET status = %s WHERE id = %s",
            (novo_status, id)
        )
        conexao.commit()
        sucesso = cursor.rowcount > 0
    except mysql.connector.Error as erro:
        print(f"Erro ao atualizar status do agendamento: {erro}")
        if conexao is not None:
            conexao.rollback()
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()
    return sucesso


def cadastrar_agendamento(agendamento):
    """
    Insere um novo agendamento no banco de dados a partir de um
    objeto Agendamento (usa converte_tupla() da classe Agendamento).

    Retorna True se o cadastro foi feito com sucesso, ou False em caso de erro.
    """
    conexao = None
    cursor = None
    sucesso = False
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = """
            INSERT INTO agendamentos
                (cliente, telefone, servico, preco, barbeiro, data, horario, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, agendamento.converte_tupla())
        conexao.commit()
        sucesso = True
    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar agendamento: {erro}")
        if conexao is not None:
            conexao.rollback()
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()
    return sucesso


def listar_por_status(status):
    """
    Retorna uma lista de objetos Agendamento cujo status
    corresponde ao valor informado (ex.: 'Agendado', 'Concluído', 'Cancelado').
    """
    conexao = None
    cursor = None
    lista = []
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id, cliente, telefone, servico, preco, barbeiro,
                   data, horario, status
            FROM agendamentos
            WHERE status = %s
            ORDER BY data, horario
        """, (status,))
        resultados = cursor.fetchall()
        lista = [Agendamento.reverte_tupla(linha) for linha in resultados]
    except mysql.connector.Error as erro:
        print(f"Erro ao listar agendamentos por status: {erro}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()
    return lista
