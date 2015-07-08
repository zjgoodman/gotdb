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
	rm -f  *.pyc
	rm -f  models.html
	rm -f  IDB.log
	rm -rf __pycache__
	rm -f  TestIDB.out

config:
	git config -l

models.html: proj3site/populate_content/models.py
	pydoc3 -w models

idb.log:
	git log > IDB.log

requirements:
	pip install -r requirements.txt

runserver:
	proj3site/manage.py runserver 0.0.0.0:8000

sha:
	git rev-parse HEAD
fake:
	python proj3site/manage.py migrate --fake

testserver:
	python proj3site/manage.py makemigrations
	python proj3site/manage.py migrate
	python proj3site/manage.py runserver

unittest: tests.py
	python proj3site/manage.py test proj3site/populate_content
