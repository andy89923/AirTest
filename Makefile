
install: requirement.txt
	pip install -r requirement.txt

run:
	python testing.py --device Android:// --log $(shell date +'%Y%m%d-%H%M').log -r 50


DEBUG=10
INFO=20
WARN=30
ERROR=40
FATAL=50

test:
	python testing.py --device Android:// --log test.log --level $(DEBUG) -r 1