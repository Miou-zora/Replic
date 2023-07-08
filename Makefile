##
## @Miou-zora Project, Mirror-Generator, 2023
## ROOT/Makefile
## File description:
## main Makefile with main use
## rules: 
## 		tests_run: run unit tests
## 		tclean: remove files/folder created by tests execution
##		clean: remove unecessary files 
##		fclean: make clean and remove binary files

TESTS_HTML_FOLDER	=	tests_html

RM					=	rm -rf

install:
	pip install -r requirements.txt

coding_style:
	@echo "Coding style checking..."
	@python3 -m pycodestyle --statistics

coding_style_details:
	@echo "Coding style checking..."
	@python3 -m pycodestyle --show-source --show-pep8

tests_run:
	@python3 -m coverage run -m pytest
	@python3 -m coverage report --precision=4
	@python3 -m coverage html -d $(TESTS_HTML_FOLDER)

tclean:
	$(RM) .coverage
	$(RM) .pytest_cache

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	$(RM) $(TESTS_HTML_FOLDER)/*

fclean: clean tclean

.PHONY: install tests_run tclean clean fclean
