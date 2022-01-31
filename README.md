## BD_Northwind_Django

### Project for studies

The aim of the project is to implement a system that performs basic operations
in the sample Northwind database using python, framework django and postgreSQL.
Northwind database is well-known version of the Microsoft Northwind sample database.

The Northwind database is an excellent schema for a
small-business ERP, with categories, customers, region, territories,
employees, shippers, suppliers, products and orders.

## How to run application

### Download Repository

Clone Repository
```bash
git clone << Repository Url>>
```
Change the working directory to the repository
```bash
cd Projekt_BD_Northwind
```

### Python

Check if python and pip are installed:
```bash
python --version
pip --version
```
If not, please install the latest version of python3 and pip
Location of python, pip and virtualenv should be in $PATH

### Create the virtual environemnt and install required packages

Check if virtualenv is installed
```bash
python -m virtualenv --version
```
if not please install
```bash
pip install virtualenv
```
In downloaded folder of repo, please create virtualenv
```bash
virtualenv venv
```
Next step is activation of venv. Please run activation script in venv directory
```bash 
venv\Scripts\activate 
```
This could be necessary to run script
```bash 
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
After activation command promt will be modified. You could run scripts and install packages for create venv
Install requirements
```bash 
pip install -r requirements.txt
```

### Notes for Postgres

Please install postgreSQL.
Enter to postgres shell from 'SQL SHELL (psql)',
or via command line, if added to $PATH
```bash
psql -U postgres
```
Create user for Postgres
```bash
CREATE ROLE NORTHWIND_USER WITH LOGIN ENCRYPTED PASSWORD 'NORTHWIND_PASSWORD';
```
Create database for Postgres
```bash
CREATE DATABASE northwind_database WITH OWNER = NORTHWIND_USER;
```

Default configuration for Postgres database. Configuration located in file BD_Northwind_Django/settings.py
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'northwind_database',
        'USER': 'northwind_user',
        'PASSWORD': 'NORTHWIND_PASSWORD',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Runserver

Use the runserver command in venv to launch the application
```bash
python manage.py runserver
```
Run server at http://127.0.0.1:8000/

### Migrations
Create the schemas for the databases
```bash
python manage.py makemigrations
python manage.py migrate
```

### Populate the database with sample data
```bash
python manage.py loaddata resources/fixtures/northwind.json --app northwind
```

## Files

* Diagram:
    * resources/diagram/northwind_ERD.png
* Data:
    * Sample data for django
        * resources/fixtures/northwind.json
