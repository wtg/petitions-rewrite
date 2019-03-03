Check the [Wiki](https://github.com/wtg/petitions-rewrite/wiki) for Django references and more documentation.

#### Installation:

1. Clone the repository and switch into the new directory:
    ```
    git clone https://github.com/wtg/petitions-rewrite.git
    cd petitions-rewrite
    ```

2. Install the python 3.6 or greater 
    ```
    sudo apt install python<python_version> python3-pip -y
    ```

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

7. Set up the local database

    * Install [SQLite](https://www.sqlite.org/) for your operating system.

    * Set the `DJANGO_SETTINGS_MODULE` environment variable to use the settings file for development (petitions/settings/dev.py):
    ```
    export DJANGO_SETTINGS_MODULE='petitions.settings.dev'
    ```

    * Make migrations:
    ```
    python manage.py makemigrations index
    python manage.py migrate
    ```

    * Add an admin user - `python manage.py createsuperuser`

7. Run the site: 
    ```
    python manage.py runserver
    ```
    Navigate to http://localhost:8000 to view. Go to http://localhost:8000/admin to add test data.

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
