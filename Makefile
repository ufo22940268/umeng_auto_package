all:
	python umeng.py

.PHONY: test
test:
	python test.py

.DEFAULT_GOAL := test

