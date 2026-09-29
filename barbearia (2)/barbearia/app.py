# app.py
# Aplicação Flask da Barbearia

from flask import Flask, render_template, request, redirect, url_for
from agendamentos import (
    listar_agendamentos,
    buscar_agendamento,
    listar_por_status,
    cadastrar_agendamento,
    atualizar_status,
)
from models import Agendamento

app = Flask(__name__)

NOME_BARBEARIA = "Barbearia Navalha de Ouro"


@app.route("/")
def index():
    """Página inicial: nome da barbearia e total de agendamentos."""
    agendamentos = listar_agendamentos()
    return render_template("index.html",
                            nome_barbearia=NOME_BARBEARIA,
                            agendamentos=agendamentos)


@app.route("/agendamentos")
def agendamentos_view():
    """Exibe a tabela com todos os agendamentos."""
    agendamentos = listar_agendamentos()
    return render_template("agendamentos.html",
                            nome_barbearia=NOME_BARBEARIA,
                            agendamentos=agendamentos,
                            status_atual=None)


@app.route("/agendamentos/status/<status>")
def agendamentos_por_status(status):
    """Exibe os agendamentos filtrados por status."""
    agendamentos = listar_por_status(status)
    return render_template("agendamentos.html",
                            nome_barbearia=NOME_BARBEARIA,
                            agendamentos=agendamentos,
                            status_atual=status)


@app.route("/agendamento/novo", methods=["GET", "POST"])
def novo_agendamento():
    """
    GET  -> exibe o formulário de cadastro de um novo agendamento.
    POST -> valida os dados enviados, cria o objeto Agendamento e
            grava no banco através de cadastrar_agendamento().
    """
    erro = None

    if request.method == "POST":
        # Coleta e limpeza básica dos dados vindos do formulário
        cliente = request.form.get("cliente", "").strip()
        telefone = request.form.get("telefone", "").strip()
        servico = request.form.get("servico", "").strip()
        preco = request.form.get("preco", "").strip()
        barbeiro = request.form.get("barbeiro", "").strip()
        data = request.form.get("data", "").strip()
        horario = request.form.get("horario", "").strip()
        status = request.form.get("status", "Agendado").strip()

        # Validação simples dos campos obrigatórios (cliente e data)
        if not cliente or not data:
            erro = "Cliente e data são campos obrigatórios."
        else:
            try:
                preco_convertido = float(preco) if preco else 0.0
            except ValueError:
                preco_convertido = 0.0
                erro = "Preço inválido. Foi salvo como 0.00."

            agendamento = Agendamento(
                cliente=cliente,
                telefone=telefone,
                servico=servico,
                preco=preco_convertido,
                barbeiro=barbeiro,
                data=data,
                horario=horario,
                status=status or "Agendado",
            )

            sucesso = cadastrar_agendamento(agendamento)
            if sucesso:
                # Redireciona para a listagem após salvar (evita reenvio do form no F5)
                return redirect(url_for("agendamentos_view"))
            else:
                erro = "Não foi possível cadastrar o agendamento. Tente novamente."

    return render_template("novo.html",
                            nome_barbearia=NOME_BARBEARIA,
                            erro=erro)


@app.route("/agendamento/<int:id>")
def agendamento_detalhe(id):
    """Exibe o detalhe de um agendamento específico."""
    agendamento = buscar_agendamento(id)
    return render_template("detalhe.html",
                            nome_barbearia=NOME_BARBEARIA,
                            agendamento=agendamento)


@app.route("/agendamento/<int:id>/status/<novo_status>", methods=["POST"])
def mudar_status(id, novo_status):
    """
    Atualiza o status de um agendamento (ex.: Cancelado ou Concluído)
    e volta para a página de detalhe.
    """
    if novo_status in ("Agendado", "Concluído", "Cancelado"):
        atualizar_status(id, novo_status)
    return redirect(url_for("agendamento_detalhe", id=id))


if __name__ == "__main__":
    app.run(debug=True)
