# Livraria API

Este projeto é uma API simples que simula uma livraria, construída utilizando o framework FastAPI. A API permite a gestão de clientes, livros, autores e vendas.

## Funcionalidades

- **Gerenciamento de Clientes**: Criação e leitura de informações dos clientes.
- **Gerenciamento de Livros**: Criação e leitura de informações dos livros.
- **Gerenciamento de Autores**: Criação e leitura de informações dos autores.
- **Registro de Vendas**: Criação e consulta de registros de vendas realizadas.

## Estrutura do Projeto

O projeto é composto pelas seguintes classes principais:

### `Client`

Representa um cliente da livraria.

- **Atributos:**
  - `id`: Identificador único.
  - `name`: Nome do cliente.
  - `email`: Email do cliente.

### `Book`

Representa um livro disponível na livraria.

- **Atributos:**
  - `id`: Identificador único.
  - `title`: Título do livro.
  - `author_id`: Identificador único do autor do livro.

### `Author`

Representa um autor cujos livros estão disponíveis na livraria.

- **Atributos:**
  - `id`: Identificador único do autor.
  - `name`: Nome do autor.

### `Sale`

Representa uma venda realizada na livraria.

- **Atributos:**
  - `id`: Identificador único da venda.
  - `client_id`: Identificador único do cliente que realizou a compra.
  - `book_id`: Identificador único do livro vendido.

## Pré-requisitos

Antes de iniciar, você precisará ter o Python 3.8+ instalado em sua máquina. Recomenda-se utilizar um ambiente virtual para isolar as dependências do projeto.

## Instalação

1. Clone o repositório:

   ```
   git clone https://github.com/seu-usuario/livraria-api.git
   cd livraria-api
   
2. Crie e ative um ambiente virtual:

    ```
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:

    ```
     pip install -r requirements.txt
    ```

5. Execute a aplicação:

    ```
     uvicorn main:app --reload
    ```

A API estará disponível em http://127.0.0.1:8000.

## Endpoints
Cliente

    POST /api/clients/: Cria um novo cliente.
    GET /api/clients/: Retorna as informações de todos os clientes.
    GET /api/clients/{client_id}: Retorna as informações de um cliente específico.

Livro

    POST /api/books/: Cria um novo livro.
    GET /api/books/: Retorna as informações de todos os livros.
    GET /api/books/{book_id}: Retorna as informações de um livro específico.

Autor

    POST /api/authors/: Cria um novo autor.
    GET /api/authors/: Retorna as informações de todos os autores.
    GET /api/authors/{author_id}: Retorna as informações de um autor específico.

Venda

    POST /api/sales/: Registra uma nova venda.
    GET /api/sales/{sale_id}: Retorna as informações de uma venda específica.
    GET /api/sales/by_book/{book_id}: Retorna as informações de todas as vendas a partir do ID de um livro.
    GET /api/sales/by_client/{client_id}: Retorna as informações de todas as vendas a partir do ID de um cliente.

A documentação swagger da API está disponível em http://127.0.0.1:8000/docs.
