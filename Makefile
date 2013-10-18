all:
	python umeng.py

.PHONY: test
test:
	python test.py


doc:
	markdown README.md > /tmp/a.html

.DEFAULT_GOAL := test

