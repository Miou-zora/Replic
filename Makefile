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

COLOR_GREEN			=	"\033[1;32m"

COLOR_RED			=	"\033[1;31m"

DEFAULT				=	"\033[0m"

install:
	pip install -r requirements.txt

coding_style:
	@printf "Coding style checking...\n"
	@if python3 -m pycodestyle --statistics --exclude=test; then \
		printf ${COLOR_GREEN}"[OK]\n"${DEFAULT}; \
	else \
		printf ${COLOR_RED}"[KO]\n"${DEFAULT}; \
		exit 1; \
	fi

coding_style_details:
	@printf "Coding style checking...\n"
	@python3 -m pycodestyle --show-source --show-pep8 --exclude=test
	@printf ${COLOR_GREEN}"[OK]\n"${DEFAULT}

tests_run:
	@python3 -m coverage run -m pytest
	@python3 -m coverage report --precision=4
	@python3 -m coverage html -d $(TESTS_HTML_FOLDER)
	python3 -m unittest discover -s tests

tclean:
	$(RM) .coverage
	$(RM) .pytest_cache

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	$(RM) $(TESTS_HTML_FOLDER)/*

fclean: clean tclean

.PHONY: install tests_run tclean clean fclean
