# Django Pseudonymization Example

## Data Masking via Custom Fields

This example Django app demonstrates an approach to pseudonymizing personal data using custom fields on the model.

### Implementation

The general steps involved in this approach:

- Create a custom User class
- Create a custom Field class
  - `__init__` and `deconstruct`
  - `get_internal_type`
  - `get_prep_value` and `from_db_value`
- Alter the model fields used for storage of values to be masked

...

For a more detailed explanation, check out the [blog post](https://www.cuttlesoft.com/data-pseudonymization-in-django/#example-2) on [Cuttlesoft.com](https://www.cuttlesoft.com/data-pseudonymization-in-django/#example-2).

## Clone and Checkout

```bash
git clone https://github.com/cuttlesoft/django-pseudonymization-example.git
cd django-pseudonymization-example
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
createdb django_pseudonymization_fields
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

## License

MIT

## Wanna Cuttle?

- 🐙 [Cuttlesoft.com](https://cuttlesoft.com)
- 🐦 [@cuttlesoft](https://twitter.com/cuttlesoft)
- 📩 hello [at] cuttlesoft [dot] com
