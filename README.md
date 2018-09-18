### Installation:

1. Clone the repository: `git clone https://github.com/wtg/petitions-rewrite.git`<br>
Then `cd petitions-rewrite`

2. Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/).

    * Create the virtual environment with python 3.5 or greater: `virtualenv --python=/usr/bin/<PYTHON_VERSION> petitions-env`

3. Activate the virtual environment: `source petitions-env/bin/activate`

4. Install [Django](https://www.djangoproject.com/download/): `pip install django`<br>
Verify that it was successfully installed: `python -c "import django; print(django.get_version())"`

5. Configuration:
    * [Create a secret key](https://django-generate-secretkey.readthedocs.io/en/latest/)
    * Rename `conf.json.sample` to `conf.json`
    * Add the secret key generate above to `conf.json`

6. Run the application: `python manage.py runserver`


### References

* [Server side rendered Django tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
* [Installing Django on Winodws Subsystem for Linux (WSL)](https://www.youtube.com/watch?v=Z4D7Mv-MuNg)