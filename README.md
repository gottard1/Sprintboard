# SprintBoard - Quadro Kanban com Python/Flask

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue?style=for-the-badge&logo=postgresql&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=for-the-badge&logo=javascript&logoColor=black)

Um quadro Kanban interativo e escalável construído com Python, Flask e PostgreSQL. Este projeto segue as melhores práticas de desenvolvimento, incluindo uma arquitetura baseada em Blueprints, princípios SOLID e um sistema de autenticação seguro.

---

## 📋 Tabela de Conteúdos

1.  [Funcionalidades](#-funcionalidades)
2.  [Tecnologias Utilizadas](#-tecnologias-utilizadas)
3.  [Pré-requisitos](#-pré-requisitos)
4.  [Como Configurar e Executar o Projeto](#-como-configurar-e-executar-o-projeto)
5.  [Como Usar a Aplicação](#-como-usar-a-aplicação)
6.  [Estrutura do Projeto](#-estrutura-do-projeto)
7.  [Licença](#-licença)
8.  [Contato](#-contato)

---

## ✨ Funcionalidades

* **Autenticação de Usuários:** Sistema completo de registro e login com senhas criptografadas.
* **Visualização Kanban:** Tarefas organizadas em colunas (Pendente, Em Andamento, Completa, Cancelada).
* **Drag and Drop:** Interface intuitiva para arrastar e soltar tarefas, atualizando seu status em tempo real.
* **Criação de Tarefas:** Adição de novas tarefas através de um modal dinâmico, com campos para descrição, status, urgência e data de entrega.
* **Arquitetura Profissional:** Código organizado em módulos (Blueprints) e camadas (Repository, Service), seguindo os princípios SOLID para alta manutenibilidade e escalabilidade.

---

## 🚀 Tecnologias Utilizadas

* **Backend:** Python 3, Flask
* **Banco de Dados:** PostgreSQL
* **Driver do Banco:** Psycopg 3
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
* **Segurança:** Flask-Bcrypt para hashing de senhas
* **Gerenciamento de Ambiente:** python-dotenv

---

## 🔧 Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes softwares instalados na sua máquina:

* [Python 3.10+](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/) (um servidor rodando localmente ou acessível)
* [Git](https://git-scm.com/downloads/)

---

## ⚙️ Como Configurar e Executar o Projeto

Siga este passo a passo para deixar o ambiente pronto para execução.

### 1. Clonar o Repositório
```bash
git clone [https://seu-repositorio-aqui.git](https://seu-repositorio-aqui.git)
cd nome-do-projeto
```

### 2. Criar e Ativar o Ambiente Virtual
É uma boa prática isolar as dependências do projeto.

* **No macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
* **No Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 3. Instalar as Dependências
Com o ambiente virtual ativado, instale todos os pacotes necessários.
```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados PostgreSQL
Você precisa ter um banco de dados e um usuário criados no PostgreSQL.

* Abra o `psql` ou sua ferramenta de banco de dados preferida e execute:
    ```sql
    -- Crie um novo banco de dados (se ainda não existir)
    CREATE DATABASE sprintboard_db;

    -- Crie um novo usuário com uma senha segura
    CREATE USER `seu_user` WITH PASSWORD `sua_senha`;

    -- Dê ao usuário todas as permissões no novo banco
    GRANT ALL PRIVILEGES ON DATABASE sprintboard_db TO `seu_user`;
    ```
    *Lembre-se de substituir os nomes e a senha se desejar.*

### 5. Configurar as Variáveis de Ambiente
As credenciais do banco e outras chaves secretas são gerenciadas por um arquivo `.env`.

1.  Renomeie o arquivo de exemplo `.env.example` (se existir) para `.env`. Se não existir, crie um novo arquivo chamado `.env` na raiz do projeto.
2.  Preencha o arquivo `.env` com suas credenciais:

    ```env
    # Configuração do Ambiente Flask
    FLASK_APP=run.py
    FLASK_ENV=development
    FLASK_DEBUG=1

    # Chave secreta para sessões
    SECRET_KEY='sua-chave-secreta-super-segura-e-dificil-de-adivinhar'

    # URL de Conexão com o Banco de Dados PostgreSQL
    # Formato: postgresql://<usuario>:<senha>@<host>:<porta>/<nome_do_banco>
    DATABASE_URL='postgresql://`seu_user`:`sua_senha`sprintboard""@localhost:5432/sprintboard_db'
    ```

### 6. Inicializar o Banco de Dados
Execute o script `init_db.py` para criar as tabelas `users` e `tasks`. **Execute este comando apenas uma vez.**
```bash
python init_db.py
```

### 7. Executar a Aplicação
Agora, com tudo configurado, inicie o servidor Flask.
```bash
python run.py
```
A aplicação estará rodando em `http://127.0.0.1:5000`.

---

## 🕹️ Como Usar a Aplicação

1.  Acesse `http://127.0.0.1:5000` no seu navegador.
2.  Você será direcionado para a página de login. Clique em "Registre-se" para criar uma nova conta.
3.  Após o registro, você será automaticamente logado e redirecionado para o quadro Kanban.
4.  Para criar uma nova tarefa, clique no botão **"+ Nova Tarefa"** no cabeçalho.
5.  Preencha o formulário no modal e clique em "Salvar Tarefa".
6.  Para mudar o status de uma tarefa, simplesmente **clique e arraste** o card para a coluna desejada. A alteração é salva automaticamente.

---

## 🏛️ Estrutura do Projeto

O projeto utiliza uma arquitetura modularizada para facilitar a manutenção e o crescimento.

* `run.py`: Ponto de entrada da aplicação.
* `app/`: Contém o núcleo da aplicação.
    * `__init__.py`: Application Factory (`create_app`) que monta a aplicação.
    * `modules/`: Cada subpasta é um **Blueprint** (módulo), como `tasks` e `users`.
        * `routes.py`: Define as URLs e a lógica de visualização.
        * `services.py`: Contém a lógica de negócio (regras da aplicação).
        * `repository.py`: Responsável pela comunicação com o banco de dados.
        * `interfaces.py`: Define os contratos (SOLID) para desacoplar as camadas.
        * `models.py`: Define as estruturas de dados.
* `instance/`: Contém arquivos de configuração que não devem ir para o controle de versão.

---

## 📜 Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.

---

## 👤 Contato

Marcel Anesi - [Seu Email](mailto:marcel.id22@gmail.com) - [Seu LinkedIn](https://linkedin.com/in/marcel-felipe)
