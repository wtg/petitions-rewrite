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

Check the [Wiki](https://github.com/wtg/petitions-rewrite/wiki) for Django references and more documentation.
