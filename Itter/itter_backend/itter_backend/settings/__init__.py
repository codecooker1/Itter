import os

env = os.environ.get('DJANGO_ENV', 'local')

if env == 'prod':
    from .prod import *
else:
    from .dev import *