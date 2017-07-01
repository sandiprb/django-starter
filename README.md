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
  templates/        # site-specific templates
pcss/               # Post-CSS files with config.js file included
static/             # all other static files goes here
requirements.txt
package.json
build_css.sh         # Post-CSS complie script 
Makefile             # Stuff
```


## Getting Started

1. Clone
2. Create PSQL DB & update setting.py with credentials
3. migrate
4. runserver
