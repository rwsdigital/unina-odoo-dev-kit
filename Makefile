REQUIREMENTS_INSTALLED := $(CURDIR)/.installed

VIRTUALENV?=venv
ODOO_FOLDER_NAME=odoo

requirements: $(REQUIREMENTS_INSTALLED)

$(REQUIREMENTS_INSTALLED): requirements.txt
			@echo "Installing virtualenv..."
			pip install virtualenv
			@echo "Creating virtualenv..."
			test -d $(VIRTUALENV) || virtualenv $(VIRTUALENV) && $(VIRTUALENV)/bin/pip install -U pip
			@echo "Installing python-requirements..."
			$(VIRTUALENV)/bin/pip install -U -r requirements.txt | grep --line-buffered -v '^   '

			@touch $@
			@cat README.md

start: requirements
			@cd $(ODOO_FOLDER_NAME) && ../$(VIRTUALENV)/bin/docker-compose up -d

stop: requirements
			@cd $(ODOO_FOLDER_NAME) && ../$(VIRTUALENV)/bin/docker-compose stop

restart: requirements
			@cd $(ODOO_FOLDER_NAME) && ../$(VIRTUALENV)/bin/docker-compose restart

remove: requirements
			@cd $(ODOO_FOLDER_NAME) && ../$(VIRTUALENV)/bin/docker-compose down

module: requirements
			@read -p "Enter Module Name: " module; \
			cd $(ODOO_FOLDER_NAME) && ../$(VIRTUALENV)/bin/docker-compose run web odoo scaffold $$module /mnt/extra-addons

logs: requirements
			@cd $(ODOO_FOLDER_NAME) && ../$(VIRTUALENV)/bin/docker-compose logs -f

info:
			@cat README.md
