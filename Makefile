files = `find ./src ./specs -name "*.py"`

format:
	- add-trailing-comma $(files)
	- pyformat -i $(files)
	- isort -rc src specs

lint:
	flake8 $(files)

mi:
	radon mi -e "node_modules/*" $(files)

cc:
	radon cc -e "node_modules/*" $(files)

test:
	mamba specs/ --format documentation --enable-coverage && make cov

cov:
	coverage report --include 'src/*'

htmlcov:
	coverage html --include 'src/*'

xmlcov:
	coverage xml --include 'src/*'

codeclimate:
	codeclimate analyze

commit_check:
	cz check --rev-range origin/master..HEAD
