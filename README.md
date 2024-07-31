
## Installing

### Clone the project

```bash
git clone https://github.com/ptjahjana/django-auth-stocklist.git
cd django-auth-stocklist
```

### Install dependencies & activate virtualenv

#### Install dependencies

```bash
pip install -U poetry

poetry install
poetry shell
```

### Configure the settings (connection to the database, connection to an SMTP server, and other options)

1. Edit `source/app/conf/development/settings.py` if you want to develop the project.

2. Edit `source/app/conf/production/settings.py` if you want to run the project in production.

### Apply migrations

```bash
python source/manage.py migrate
python source/manage.py loaddata source/fixture.json

```

### Collect static files (only on a production server)

```bash
python source/manage.py collectstatic
```

### Running

#### A development server

Just run this command:

```bash
python source/manage.py runserver
```
