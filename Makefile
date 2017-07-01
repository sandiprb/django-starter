export LC_CTYPE="en_US.UTF-8"

migrate:
	@cd base && python manage.py migrate --noinput

run:
	cd base && python manage.py runserver

css:
	sh ./build_css.sh


clean:
	find . -name "*.pyc" -delete

deps:
	yarn
	pip install -r requirements.txt
	make css
	make migrate
	python base/manage.py collectstatic --noinput --clear
	python base/manage.py compress
