

tests_run:
	@coverage run -m unittest discover -v -s . -t .
	@coverage report --precision=4

fclean:

tclean:
	$(RM) .coverage
