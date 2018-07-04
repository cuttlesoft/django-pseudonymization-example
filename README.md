# Django Pseudonymization Example

This example Django app demonstrates two approaches to pseudonymizing personal data with masking functions.

- [Example 1](https://github.com/cuttlesoft/django-pseudonymization-example/tree/properties) employs getter and setter methods to interface with the pseudonymized model fields.
- [Example 2](https://github.com/cuttlesoft/django-pseudonymization-example/tree/fields) creates a custom Field class to handle value masking/unmasking automatically.

...

For a more detailed explanation, check out the [blog post](https://www.cuttlesoft.com/data-pseudonymization-in-django) on [Cuttlesoft.com](https://www.cuttlesoft.com/data-pseudonymization-in-django).

## Clone

```bash
git clone https://github.com/cuttlesoft/django-pseudonymization-example.git
cd django-pseudonymization-example
```

### Checkout Example Branches

[Example 1](https://github.com/cuttlesoft/django-pseudonymization-example/tree/properties), branch: `properties`

```bash
git checkout properties
```

[Example 2](https://github.com/cuttlesoft/django-pseudonymization-example/tree/fields), branch: `fields`

```bash
git checkout fields
```

## Dependencies

This example uses Django 2.0, which supports Python 3.4, 3.5, and 3.6. To properly run this example you'll need:

1.  Python 3.4 or greater
2.  [PostgreSQL](https://www.postgresql.org/)
3.  [pipenv](https://docs.pipenv.org/)

Install dependencies with `pipenv`

```bash
$ pipenv install
Creating a virtualenv for this project…
...
Virtualenv location: /Users/user/.venvs/django-pseudonymization-example-ztyUS4al
Installing dependencies from Pipfile.lock (5d8b51)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 3/3 — 00:00:09
To activate this project's virtualenv, run the following:
 $ pipenv shell
```

Activate virtual environment with `pipenv`

```bash
$ pipenv shell
Spawning environment shell (/bin/zsh). Use 'exit' to leave.
(django-pseudonymization-example-ztyUS4al) $
```

## Initialize the Application

```bash
createdb django_pseudonymization_example
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Start the Application

```bash
$ python manage.py runserver

Performing system checks...

System check identified no issues (0 silenced).
June 25, 2018 - 21:16:11
Django version 2.0.6, using settings 'app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Disclaimer

Our `mask`/`unmask` functions are intended for this example only, to enable demonstration of the application's handling of masking and unmasking. They do not sufficiently protect the data, as it is reasonably likely that someone accessing the data would be able to simply reverse the shifted characters, re-identifying users without any additional information present.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)
file for details

## Wanna Cuttle?

- 🐙 [Cuttlesoft.com](https://cuttlesoft.com)
- 🐦 [@cuttlesoft](https://twitter.com/cuttlesoft)
- 📩 hello [at] cuttlesoft [dot] com
