🌍 [Leia em Português](README.pt-BR.md)

# My Energy Api

Api rest developed with `django and django-ninja` for the `My Energy` project to perform manupilations in an oracle database.

## Technologies Used

- `Django` - API main structure.
- `Django Ninja` - Framework for fast and efficient construction of REST APIs.
- `SQLite` - Standard database (can be changed as needed).

## Functionalities

The API offers a number of features for handling and managing data. Some of the main features include:

- Creation of new records in the database.
- Querying existing data through filters and parameters.
- Update of specific records.
- Deletion of data.

## Installation & Configuration

1. Clone the repository:

```bash
git clone https://github.com/felipeclarindo/my-energy-api.git
```

2. Enter directory:

```bash
cd my-energy-api
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure Database and Migrations:

```bash
python manage.py migrate
```

5. Run the server:

```bash
python manage.py runserver
```

6. Access the API in http://localhost:8000/api.

7. Go to [My Energy Repository](https://github.com/felipeclarindo/my-energy) to run the front end.

## Contribution

Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request.

## Author

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## License

This project is licensed under the [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
