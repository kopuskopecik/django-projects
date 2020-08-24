from .base import *
from decouple import config, Csv


INSTALLED_APPS += (
	# Proje içi appler
	'accounts',
	'lessons',
	#3. Parti Paketler
	"debug_toolbar",
	'crispy_forms',
	'ckeditor',
	)

MIDDLEWARE += (
	 'debug_toolbar.middleware.DebugToolbarMiddleware',
	)
	

INTERNAL_IPS = [
	'127.0.0.1',
]
	

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


AUTH_USER_MODEL = 'accounts.User'

LOGIN_URL = 'accounts:login'

LOGOUT_URL = 'accounts:logout'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'


CRISPY_TEMPLATE_PACK = "bootstrap4"


CKEDITOR_jQUERY_URL = os.path.join(STATIC_URL, "js/jquery9.min.js")
CKEDITOR_CONFIGS = {
	'default': {
		'toolbar': 'full',
		'width':'100%',
		'height':'50%',
		'codeSnippet_theme':'school_book',
	},
}

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}