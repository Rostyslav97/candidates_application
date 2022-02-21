# Candidates experience REST API application

# Setup

## Mandatory steps
1. Install Python3.9+
2. Install Pipenv

## Setup project
Install environment
```bash
# Create virtual environment
virtualenv venv
source venv/bin.activate

#pip install --dev
pip install requirements.txt
```

Run django server
```bash
# Run migrations only on a project setup
python manage.py migrate

# Run server
python manage.py runserver
```