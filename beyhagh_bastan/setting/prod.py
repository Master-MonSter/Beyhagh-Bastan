from beyhagh_bastan.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v8!i8204e5_v@_n82#d_2k@_92pn8=*5aqgvfu4-v3z0zr3hw@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 2 # Using site id for site framework

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# ******************************** reset password with email ********************************
# !!!  C u o t i o n  !!! We must change some lines on the auth.views and moddified app name on th password_reset_email.html in PasswordResetEmail class
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"    # With console
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"         # With email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_POST = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER ='beyhagh.bastan.antique@gmail.com'
EMAIL_HOST_PASSWORD ='byxy leux imad acea' # From beyhagh.bastan.antique@gmail.com
# ******************************** reset password with email ********************************

# ************************************** Django-compressor **************************************
STATICFILES_FINDERS = (
        # other finders..
        'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True
COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]
if not COMPRESS_ENABLED:
       COMPRESS_ENABLED = True
       COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
       COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]
# ************************************** Django-compressor **************************************