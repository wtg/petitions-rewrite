### Installation:

1. Clone the repository: `git clone https://github.com/wtg/petitions-rewrite.git`<br>
Then `cd petitions-rewrite`

2. Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

    * Install the latest version of python: `cd && sudo apt install python3.7 python3-pip -y`
   
    * Make python 3.* the default version: `update-alternatives --install /usr/bin/python python /usr/bin/python3 1`
   
    * Check python version `python -V`
   
    * Create the virtual environment with python 3.5 or greater: `virtualenv --python=/usr/bin/<PYTHON_VERSION> petitions-env`
    
    * If `virtualenv --python=/usr/bin/<PYTHON_VERSION> petitions-env` fails, try `sudo apt install virtualenv` instead.

3. Activate the virtual environment: `source petitions-env/bin/activate`

4. Install [Django](https://www.djangoproject.com/download/): `pip install django`<br>
    * Verify that it was successfully installed: `python -c "import django; print(django.get_version())"`

5. Configuration:
    * Open a terminal, and set a secret key environment variable:
<br>`export SECRET_KEY="any string will work for development"`

6. Run the site: `python manage.py runserver`<br>
Navigate to http://127.0.0.1:8000 to view


### References:

* [Server side rendered Django tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
* [Installing Django on Windows Subsystem for Linux (WSL)](https://www.youtube.com/watch?v=Z4D7Mv-MuNg)
