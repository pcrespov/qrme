

PHONY: up
up:
	python -m http.server --directory $(CURDIR)

.venv:
	python3 -m venv .venv
	.venv/bin/python3 -m pip install --upgrade pip setuptools wheel
	@echo "Type source .venv/bin/activate"

.PHONY: qr
qr:
	.venv/bin/python3 ./scripts/qr.py



## CLEAN -------------------------------

.PHONY: clean .check-clean
_git_clean_args := -dx --force --exclude=.vscode --exclude=.venv --exclude=.python-version --exclude="*keep*"

.check-clean:
	@git clean -n $(_git_clean_args)
	@echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]
	@echo -n "$(shell whoami), are you REALLY sure? [y/N] " && read ans && [ $${ans:-N} = y ]

clean: .check-clean ## cleans all unversioned files in project and temp files create by this makefile
	# Cleaning unversioned
	@git clean $(_git_clean_args)

