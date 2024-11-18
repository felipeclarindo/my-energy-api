# My Energy Api

Api Rest para realizar manupilações em um banco de dados oracle desenvolvida com `django e django-ninja`

## Tecnologias Utilizadas

Django - Estrutura principal da API
Django Ninja - Framework para construção rápida e eficiente de APIs REST
SQLite - Banco de dados padrão (pode ser alterado conforme necessidade)

## Funcionalidades da API

A API oferece uma série de funcionalidades para manipulação e gerenciamento de dados. Algumas das principais funcionalidades incluem:

- Criação de novos registros no banco de dados.
- Consulta de dados existentes por meio de filtros e parâmetros.
- Atualização de registros específicos.
- Exclusão de dados.

## Instalação e Configuração

1. Clone o Repositório:

```bash
git clone https://github.com/felipeclarindo/my-energy-api.git
cd global_solution_api
```

2. Instale as Dependências:

```bash
pip install -r requirements.txt
```

3. Configure o Banco de Dados e Migrações:

```bash
python manage.py migrate
```

4. Execute o Servidor:

```bash
python manage.py runserver
```

Acesse a API em http://localhost:8000/api.

## Front end

1. Acesse o reposiotorio

```bash
https://github.com/felipeclarindo/my-energy
```

2. Siga as intruções no repositorio para rodar o `front-end`

## Integrantes

- **Felipe** RM: 554547
- **Victor** RM: 555059
- **Jennie** RM: 554661
