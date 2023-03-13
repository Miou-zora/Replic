RM		=	rm -rf

tests_run:
	@coverage run -m unittest discover -v -s . -t .
	@coverage report --precision=4

tclean:
	$(RM) .coverage

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
