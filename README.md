# Message Board (Flask)

This is a minimal Message Board app built with Flask.

Structure:
- `app.py` — Flask app and routes
- `templates/` — Jinja2 templates (`home`, `about`, `posts`, `view_post`)
- `static/` — static assets (CSS)
- `venv/` — placeholder for virtual environment
- `requirements.txt` — Python dependencies
 - `config/` — configuration modules (`default.py`, `development.py`)

Django conversion
-----------------

This project has been converted to a Django app located in `mb_site/`.

Quick start for Django (PowerShell):

```powershell
cd "c:/Users/alllu/OneDrive/Documents/School/New folder (2)/MB/mb_site"
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r ../requirements.txt
# create the database tables
python manage.py migrate
# (optional) create a superuser for admin
python manage.py createsuperuser
# run the dev server
python manage.py runserver
```

Open `http://127.0.0.1:8000/` to view the Django Message Board. The admin is at `/admin/`.

Notes:
- The Django app is in `mb_site/board/` with templates in `board/templates/board` and static files in `board/static/board`.
- The older Flask demo remains in the repo (`app.py`) but the Django app is the current implementation.
 - The older Flask demo has been removed in favor of Django.

Loading initial data:

After migrating you can load the fixture with:

```powershell
python manage.py loaddata initial_posts.json
```

Configuration:

The project will attempt to import configuration from the `config` package by default (`config.default`).
You can override which module to load with the `APP_CONFIG_MODULE` environment variable, e.g.

```powershell
$env:APP_CONFIG_MODULE = 'config.development'
python manage.py runserver
```

Quick start (PowerShell):

```powershell
# create venv (creates the `venv` folder)
python -m venv venv
# activate
venv\Scripts\Activate.ps1
# install
pip install -r requirements.txt
# run
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

Notes:
- Posts are stored in memory — restarting the server clears them.
- For production use, add a database and configure a proper WSGI server.
"# 112-MB" 
