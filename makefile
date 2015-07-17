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
	rm -f  .coverage
	rm -f  models.html
	rm -f  IDB.log
	rm -rf __pycache__
	rm -f  TestIDB.out
	rm -f  IDB.log
	rm -f TestPopulateContent.out
	rm -f proj3site/populate_content/*.pyc
	rm -f proj3site/splash/*.pyc

config:
	git config -l

models.html: proj3site/populate_content/models.py
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

testserver: proj3site/manage.py
	python3 proj3site/manage.py makemigrations
	python3 proj3site/manage.py migrate
	python3 proj3site/manage.py runserver

runserver: proj3site/manage.py
	python3 proj3site/manage.py runserver

bgserver: proj3site/manage.py
	python3 proj3site/manage.py runserver &

unittest: proj3site/populate_content/tests.py proj3site/manage.py
	coverage3 run --source proj3site/populate_content/models.py --branch proj3site/manage.py test proj3site/populate_content
	coverage3 report -m
