from .base import *

DEBUG = False

ADMIN = (
    ('Antonio M', 'email@mydomain.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '*****',
    }
}

"""
DEBUG: Setting DEBUG to False should be mandatory for any
production environment. Failing to do so will result in
traceback information and sensitive configuration data
exposed to everyone.

ADMINS: When DEBUG is False and a view raises an exception, all
information will be sent by email to the people listed in the
ADMINS setting. Make sure to replace the name/email tuple
with your own information.
"""