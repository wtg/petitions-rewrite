from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django_cas_ng import views as baseviews


# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request, **kwargs):
    return _add_locale(request, baseviews.login(request, **kwargs))


def logout(request, **kwargs):
    return _add_locale(request, baseviews.logout(request, **kwargs))


def _add_locale(request, response):
    """If the given HttpResponse is a redirect to CAS, then add the proper
    `locale` parameter to it (and return the modified response). If not, simply
    return the original response."""

    if (
        isinstance(response, HttpResponseRedirect)
        and response['Location'].startswith(settings.CAS_SERVER_URL)
    ):
        from ourapp.some_module import get_currently_used_language
        url = response['Location']
        url += '&' if '?' in url else '&'
        url += "locale=%s" % get_currently_used_language(request)
        response['Location'] = url
    return response
