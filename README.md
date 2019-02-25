#### Installation:

1. Clone the repository and switch into the new directory:
```
git clone https://github.com/wtg/petitions-rewrite.git
cd petitions-rewrite
```

2. Install the python 3.6 or greater 
```sudo apt install python<python_version> python3-pip -y```

3. Install [pipenv](https://pipenv.readthedocs.io/en/latest/)
   
4. Create pipenv with python 3.6 or greater and install dependencies 
```
pipenv install --python <python_version>
```

5. Activate the virtual environment ```pipenv shell```

6. Set a secret key environment variable 
```
export SECRET_KEY="any string will work for development"
```

7. Run the site: ```python manage.py runserver```
Navigate to http://127.0.0.1:8000 to view

#### Making changes:

The code formatter, [Python Black](https://black.readthedocs.io/en/stable/) is now enforced on Travis builds.
To format one file, run 
```
black <path to file>
```
or to format all python files your current directory, run
```
black .
``` 
Then commit and push any changed files.

#### Setting up the local database

1. Install Postgres for your operating system.

2. Create the `petitions` database:

    * Enter `psql`. If that gives an error, try `createdb`, then `psql`
    * Create a user for this database:
    `CREATE USER '<user>' WITH PASSWORD '<password>';`
    * Create the database:
    `CREATE DATABASE petitions WITH OWNER some_user;`
    * Grant privleges to the user:
    `GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO some_user;`

3. Set the 'DATABASE_URL' environment variable:
    ```
    export DATABASE_URL='postgres://<user>:<password>@localhost/petitions'
    ```

4. Install [psycopg2](http://initd.org/psycopg/docs/install.html#prerequisites)

5. Make migrations:
    ```
    python manage.py makemigrations index
    python manage.py migrate
    ```

Check the [Wiki](https://github.com/wtg/petitions-rewrite/wiki) for Django references and more documentation.
