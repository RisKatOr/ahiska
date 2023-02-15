# python 3.11.2

    git clone https://github.com/RisKatOr/ahiska
    cd ahiska

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements/dev.txt

    cp .env.template .env

    python manage.py runserver --settings=config.settings.dev

    gunicorn config.wsgi -b 127.0.0.1:8001 --settings=config.settings.dev

    python3 manage.py collectstatic --settings=config.settings.prod

#https://github.com/python-dev-blog/game_muster