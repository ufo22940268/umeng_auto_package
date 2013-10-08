all:
	python umeng.py

.PHONY: test
test:
	python test.py && cd release/

.DEFAULT_GOAL := test

