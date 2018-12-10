from django.db import models
from django.contrib.auth.middleware import RemoteUserMiddleware


class CustomHeaderMiddleWare(RemoteUserMiddleware):
    header = 'HTTP_AUTHEUSER'


    
