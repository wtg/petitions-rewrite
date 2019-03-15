from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {}
DATABASES["default"] = dj_database_url.config(default=os.environ.get("DATABASE_URL"))
