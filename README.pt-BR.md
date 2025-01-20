🌍 [Read in English](README.md)

# My Energy Api

Api rest desenvolvida com `django` e `django-ninja` para o projeto `My Energy` para realizar manupilações em um banco de dados oracle.

## Tecnologias Utilizadas

- `Django` - Estrutura principal da API.
- `Django Ninja` - Framework para construção rápida e eficiente de APIs REST.
- `SQLite` - Banco de dados padrão (pode ser alterado conforme necessidade).

## Funcionalidades da API

A API oferece uma série de funcionalidades para manipulação e gerenciamento de dados. Algumas das principais funcionalidades incluem:

- Criação de novos registros no banco de dados.
- Consulta de dados existentes por meio de filtros e parâmetros.
- Atualização de registros específicos.
- Exclusão de dados.

## Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/felipeclarindo/my-energy-api.git
```

2. Entre no diretório:

```bash
cd my-energy-api
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados e migrações:

```bash
python manage.py migrate
```

5. Execute o servidor:

```bash
python manage.py runserver
```

6, Acesse a API em http://localhost:8000/api.

7. Acesse [Repositório My Energy](https://github.com/felipeclarindo/my-energy) para rodar o front end.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## Licença

Este projeto está licenciado sob a [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
