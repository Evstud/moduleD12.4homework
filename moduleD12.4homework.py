LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s %(levelname)s %(message)s'
            },
            'less_simple': {
                'format': '%(pathname)s'
            },
            'complex': {
                'format': '{exc_info}'
            },
            'general_formatter': {
                'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
            },
            'errors_formatter': {
                'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s {exc_info}'
            },
            'mail_formatter': {
                'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
            },
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'console2': {
                'level': 'WARNING',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'less_simple'
            },
            'console3': {
                'level': 'ERROR',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
                'formatter': 'complex'
            },
            'general_file': {
                'level': 'INFO',
                'filters': ['require_debug_false'],
                'class': 'logging.FileHandler',
                'formatter': 'general_formatter',
                'filename': '/path/to/django/general.log',
            },
            'errors_file': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'logging.FileHandler',
                'formatter': 'errors_formatter',
                'filename': '/path/to/django/errors.log',
            },
            'security_file': {
                'class': 'logging.FileHandler',
                'filters': ['require_debug_false'],
                'formatter': 'general_formatter',
                'filename': '/path/to/django/security.log',
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'formatter': 'mail_formatter',
                'class': 'django.utils.log.AdminEmailHandler'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'console2', 'console3', 'general_file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'django.request': {
                'handlers': ['errors_file', 'mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
            'django.server': {
                'handlers': ['errors_file', 'mail_admins'],
                'level': 'ERROR',
                'propagate': True, 
            },
            'django.template': {
                'handlers': ['errors_file'],
                'level': 'ERROR',
                'propagate': True, 
            },
            'django.db_backends': {
                'handlers': ['errors_file'],
                'level': 'ERROR',
                'propagate': True, 
            },
            'django.security': {
                'handlers': ['security_file'],
                'propagate': True,
            }
        }
    }