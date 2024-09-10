"""
Django settings for volantserver project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_zb=j*gses4%&l#!@1k91--%5(q53(^98$vn8cm_pgb8vzz307'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'volantapp',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist', 
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    
]

ROOT_URLCONF = 'volantserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'volantserver.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# MySQL database ----------

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'czdjuaxk_volantfootwearDATABASE',
#         'USER': 'czdjuaxk_volantuser',
#         'PASSWORD': 'volant@2024',
#         'HOST': 'localhost',   # Or the IP address of your MySQL server
#         'PORT': '3306',        # Default MySQL port
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',  # Required for `django-allauth`
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}


SOCIALACCOUNT_PROVIDERS = {}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = ''

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER =''
EMAIL_HOST_PASSWORD =''
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


from datetime import timedelta


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=3),  # Example: Set to 5 minutes
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),   # Example: Set to 1 day
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': 'your_secret_key_here',
    'AUTH_HEADER_TYPES': ('Bearer',),
}



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
JAZZMIN_SETTINGS = {
    "site_title": "Volant Footwear",  # Title of your admin site
    "site_header": "Volant Footwear",  # Header text
    "site_brand": "   ",  # Brand text in the sidebar
    # "site_brand_color": "#ffffff",  # Brand color in the sidebar
    "site_brand_classes": "d-none",  # Hide the brand text in the sidebar
    "site_logo": "./logos/volantlogo-01.png",  # Path to your site logo
    "login_logo": "./logos/volantlogo-01.png",  # Logo for the login page
    "login_logo_dark": "./logos/volantlogo-01.png",  # Dark mode logo for the login page
    "site_logo_classes": " shadow-none d-flex justify-content-center  ",  # Classes for the logo (e.g., background color)
    "login_logo_classes": "shadow-none d-flex justify-content-center w-100 ",  # Classes for the logo in the login page
    "login_logo_dark_classes": "shadow-none d-flex justify-content-center w-100 ",  # Classes for the logo in the login page
    "site_icon": './logos/Mocsicon-01.svg',  # Favicon for your site
    "welcome_sign": "Welcome to Volant footwear",  # Welcome message on the login screen
    "copyright": "volantfootwear.com",  # Copyright text in the footer
    "search_model": ["auth.User", "auth.Group"],  # Models available in the search bar
    "user_avatar": './logos/volant-title-logo.png',  # User avatar (can be a path to an image)
    
    # Top Menu Links
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.User"},
        {"app": "books"},
    ],
    
    # User Menu Links
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    
    # Sidebar
    "show_sidebar": True,  # Whether to show the sidebar
    "navigation_expanded": True,  # Whether the sidebar should be expanded by default
    "hide_apps": [],  # List of apps to hide in the sidebar
    "hide_models": [],  # List of models to hide in the sidebar
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],  # Order of apps and models in the sidebar
    
    # Custom Links in Sidebar
    "custom_links": {
        "books": [{
            "name": "Make Messages",
            "url": "make_messages",
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },
    
    # Icons for Apps and Models
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",  # Default icon for parent items
    "default_icon_children": "fas fa-circle",  # Default icon for child items
    
    # Modals and Customization
    "related_modal_active": False,  # Whether related models open in a modal
    "custom_css": None,  # Path to a custom CSS file
    "custom_js": None,  # Path to a custom JS file
    "use_google_fonts_cdn": True,  # Whether to use Google Fonts CDN
    "show_ui_builder": False,  # Whether to show the UI builder
    "changeform_format": "horizontal_tabs",  # Change form format (tabs, stacked, etc.)
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},  # Override form format for specific models
    "language_chooser": False,  # Whether to show a language chooser in the admin
}
JAZZMIN_SETTINGS["show_ui_builder"] = True


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-maroon",
    "navbar": "navbar-primary navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "yeti",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-secondary",
        "info": "btn-outline-info",
        "warning": "btn-warning",
        "danger": "btn-outline-danger",
        "success": "btn-success"
    }
}