# django-starter
Barebone Django Project Starter Kit

Django + PostGresql + Post CSS

### Directory Structure

```
README.md/
base/
  manage.py         # installed to PATH via setup.py
  settings.py       # Common Settings
  wsgi.py
  urls.py           # Main URL Config
  core/             # Core app (Includes user models)
  templates/        # site-specific templates
pcss/               # Post-CSS files with config.js file included
static/             # all other static files goes here
conf/               # Config Files
requirements.txt
package.json
build_css.sh         # Post-CSS complie script
Makefile             # Stuff
```

## Plugins Added
 - [Django Compressor](https://django-compressor.readthedocs.io/en/latest/)
 - [django-hmin](https://pypi.python.org/pypi/django-hmin/0.3.2) (HTML Minifier)
 - [pre-commit](pre-commit.com)


## Getting Started

1. Clone
2. Create PSQL DB & update setting.py with credentials
3. migrate
4. runserver

