PROJECTNAME=indydata
SRCPATH := $(CURDIR)/src
BUILDPATH := $(CURDIR)/_build
COVERAGEPATH := $(BUILDPATH)/coverage
REQUIREMENTS_RESULT := $(BUILDPATH)/.requirements.txt


.PHONY: clean
clean:
	rm -rf $(BUILDPATH)
	find $(SRCPATH) -name "*.pyc" -delete
	find $(SRCPATH) -type d -name __pycache__ -delete


.PHONY: build_dirs
build_dirs: $(BUILDPATH)


$(BUILDPATH):
	mkdir -p $(BUILDPATH)
	# Also need to make the coverage path as coverage complains if it doesnt exist already
	mkdir -p $(COVERAGEPATH)


.PHONY: requirements
requirements: $(REQUIREMENTS_RESULT)

$(REQUIREMENTS_RESULT): setup.py $(SRCPATH)/requirements/*.txt | build_dirs
	pip install -U pip wheel setuptools
	pip install --upgrade --requirement $(SRCPATH)/requirements/development.txt
	pip freeze > $@


.PHONY: setup
setup: clean requirements


.PHONY: lint
lint: requirements
	flake8 $(SRCPATH) --tee --output $(BUILDPATH)/lint.txt


.PHONY: check-format
check-format: requirements
	isort -rc -c $(SRCPATH)
	black --check $(SRCPATH)


.PHONY: format
format: requirements
	isort -rc $(SRCPATH)
	black $(SRCPATH)


.PHONY: test
test: pytest $(SRCPATH) --cov


.PHONY: sdist
sdist: requirements
	python setup.py sdist --dist-dir=$(BUILDPATH)/dist
