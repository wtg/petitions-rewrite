### Installation:

1. Clone the repository: `git clone https://github.com/wtg/petitions-rewrite.git`<br>
Then `cd petitions-rewrite`

2. Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

    * Install the latest version of python: `cd && sudo apt install python3.7 python3-pip -y`
   
    * Make python 3.* the default version: `update-alternatives --install /usr/bin/python python /usr/bin/python3 1`
   
    * Check python version `python -V`
   
    * Create the virtual environment with python 3.5 or greater: `virtualenv --python=/usr/bin/<PYTHON_VERSION> petitions-env`

3. Activate the virtual environment: `source petitions-env/bin/activate`

4. Install [Django](https://www.djangoproject.com/download/): `pip install django`<br>
    * Verify that it was successfully installed: `python -c "import django; print(django.get_version())"`

5. Configuration:
    * Open a terminal, and set a secret key environment variable:
<br>`export SECRET_KEY="any string will work for development"`

6. Run the site: `python manage.py runserver`<br>
Navigate to http://127.0.0.1:8000 to view


### Setting up the local database

1. Install [Postgres]() for your operating system.

2. Create the `petitions` database:

    * Enter `psql`. If that gives an error, try `createdb`, then `psql`
    * Create a user for this database:
    `CREATE USER some_user WITH PASSWORD 'some_password';`
    * Create the database:
    `CREATE DATABASE petitions WITH OWNER some_user;`
    * Grant privleges to the user:
    `GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO some_user;`

3. Set the environment variables:
    ```
    export DB_NAME='petitions'
    export DB_USER='some_user'
    export DB_PASSWORD='some_password'
    ```

4. Install [`psycopg2`](http://initd.org/psycopg/docs/install.html#prerequisites)

5. Populate the database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
