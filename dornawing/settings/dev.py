# from .base import *

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '23tp!29&8+=wvvrmc^n)obx=w&g2dwbpnehcitl9pl5mx$oo9r'

# # SECURITY WARNING: define the correct hosts in production!
# ALLOWED_HOSTS = ['dornawing.com', 'www.dornawing.com'] 

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SECURE_HSTS_SECONDS = 31536000

# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True

# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# SECURE_HSTS_PRELOAD = True

# try:
#     from .local import *
# except ImportError:
#     pass

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = '-*8^toybn#ywd$1j2(t+_94zcd6yl3so7notow7orjr#(h7=)+'


DEBUG = True

try:
    from .local import *
except ImportError:
    pass