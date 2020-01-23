files = `find src test -name '*.py'`

format:
	add-trailing-comma $(files)
	pyformat -i $(files)
	isort -rc src test

lint:
	flake8 src test

mi:
	radon mi -e "node_modules/*" src

cc:
	radon cc -e "node_modules/*" src
