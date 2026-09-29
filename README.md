# Sistema de Agendamentos - Barbearia Navalha de Ouro

Sistema web para gerenciar os agendamentos da barbearia, substituindo o
controle manual em caderno. Desenvolvido em Python + Flask + MySQL + Jinja2.

## Estudantes

Lucas Beda, Matheus Baratieri, Arhur Flores, João Ruon.

## Como rodar

1. Instale as dependências: `pip install flask mysql-connector-python`
2. Ajuste as credenciais em `config.py`
3. Execute `banco.sql` no MySQL Workbench (cria o banco e os dados de exemplo)
4. Rode `python app.py`
5. Acesse `http://127.0.0.1:5000`
6. Para rodar os testes: `python -m unittest test_models.py -v`

## Estrutura do projeto

```
barbearia/
├── config.py          # credenciais do banco (H2)
├── banco.py            # função conectar() (H4, H11)
├── models.py            # classe Agendamento - POO (H5, H10, H13)
├── agendamentos.py       # camada de acesso a dados / DAO (H4, H8, H11)
├── app.py                 # aplicação Flask - rotas/controller (H3, H12)
├── test_models.py         # testes unitários (H9)
└── templates/
    ├── index.html
    ├── agendamentos.html
    ├── novo.html
    └── detalhe.html         # Jinja2 (H3, H12)
```

## Mapeamento dos critérios de avaliação

| Critério | Onde está aplicado |
|---|---|
| **H1** - Reconhecer ferramentas | PyCharm (IDE), MySQL Workbench, Flask, Jinja2 usados de forma integrada |
| **H2** - Instalar ferramentas conforme requisitos | Instalação de `flask` e `mysql-connector-python` via interpretador do PyCharm; configuração do MySQL Server |
| **H3** - Aplicar linguagem via IDE | Todo o projeto escrito e executado a partir do PyCharm |
| **H4** - Integrar banco de dados via linguagem | `banco.py` (conexão) + `agendamentos.py` (SELECT/INSERT com `mysql.connector`) |
| **H5** - Métodos e técnicas de programação | Classe `Agendamento` com métodos `exibir()`, `converte_tupla()`, `reverte_tupla()` (staticmethod) |
| **H6** - Comentários para documentação | Docstrings e comentários em todos os `.py` explicando cada função/módulo |
| **H7** - IDE para rastreabilidade do código | Uso do PyCharm para navegar entre definições (Ctrl+clique), debugger e Run/Debug |
| **H8** - Identificar erros conforme requisito | `try/except mysql.connector.Error/finally` em todas as funções de banco; validação de formulário em `novo_agendamento()` (campos obrigatórios, conversão de preço) |
| **H9** - IDE para teste unitário | `test_models.py` com `unittest`, executável direto pelo PyCharm |
| **H10** - Padrão de projeto | Separação em camadas no estilo **MVC**: `models.py` (Model), `templates/` (View), `app.py` (Controller), `agendamentos.py` (DAO) |
| **H11** - Integração de aplicações com banco na estruturação do sistema | Fluxo completo: formulário (`novo.html`) → rota Flask → `cadastrar_agendamento()` → `INSERT` no MySQL |
| **H12** - Frameworks para desenvolvimento | Flask (rotas/backend) + Jinja2 (templates dinâmicos: `{% for %}`, `{% if %}`, `url_for()`) |
| **H13** - Especificações técnicas e paradigmas | Paradigma orientado a objetos (classe `Agendamento`) combinado com o paradigma imperativo/procedural nas rotas Flask |

## Funcionalidades

- Página inicial com nome da barbearia e total de agendamentos
- Listagem de todos os agendamentos, com destaque visual por status
  (verde = Concluído, vermelho = Cancelado)
- Filtro de agendamentos por status
- Cadastro de novo agendamento via formulário
- Página de detalhe de um agendamento específico (com tratamento de
  "não encontrado")
