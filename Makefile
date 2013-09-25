all:
	python umeng.py

.PHONY: test
test:
	python test.py && cd release/ &&  python -m SimpleHTTPServer

.DEFAULT_GOAL := test

