
TESTS_HTML_FOLDER	=	tests_html

RM					=	rm -rf

tests_run:
	@coverage run -m pytest -v
	@coverage report --precision=4
	@coverage html -d $(TESTS_HTML_FOLDER)

tclean:
	$(RM) .coverage
	$(RM) .pytest_cache

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	$(RM) $(TESTS_HTML_FOLDER)/*

fclean: clean
