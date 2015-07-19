FILES :=                             \
    .gitignore						 \
	.travis.yml                      \
	apiary.apib						 \
	IDB.log							 \
	models.html                      \
	models.py                        \
	tests.py                         \
	UML.pdf                          \

all:

check:
	@for i in $(FILES);                                         \
    do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

clean:
	rm -rf proj3site/populate_content/migrations
	rm -rf proj3site/populate_content/__pycache__

html: proj3site/populate_content/models.py
	pydoc3 -w models

log:
	git log > IDB.log

requirements: requirements.txt
	pip3 install -r requirements.txt

deploy: proj3site/manage.py
	python3 proj3site/manage.py runserver 0.0.0.0:80 &

sha:
	git rev-parse HEAD

soup: soupscraper.py
	python soupscraper.py > soup.out

fake: proj3site/manage.py
	python3 proj3site/manage.py migrate --fake
	python3 proj3site/manage.py migrate

migrations: proj3site/manage.py
	python3 proj3site/manage.py makemigrations
	python3 proj3site/manage.py migrate

runserver: proj3site/manage.py
	python3 proj3site/manage.py runserver

unittest: proj3site/populate_content/tests.py proj3site/manage.py
	coverage3 run --source proj3site/populate_content/models.py --branch proj3site/manage.py test proj3site/populate_content
	coverage3 report -m
