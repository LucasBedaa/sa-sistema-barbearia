# banco.py
# Responsável pela conexão com o banco de dados MySQL

import mysql.connector
from config import DB_CONFIG


def conectar():
    """
    Abre e retorna uma conexão com o banco de dados MySQL,
    utilizando as credenciais definidas em config.py.
    """
    conexao = mysql.connector.connect(**DB_CONFIG)
    return conexao
