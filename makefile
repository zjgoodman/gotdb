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

models.html: models.py
	pydoc3 -w IDB

IDB.log:
	git log > IDB.log

SHA:
	git rev-parse HEAD

TestIDB.out: tests.py
	coverage3 run --omit=*numpy* --branch tests.py >  TestIDB.out 2>&1
	coverage3 report -m                      >> TestIDB.out
	cat TestIDB.out