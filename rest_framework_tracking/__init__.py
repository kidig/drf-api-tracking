__version__ = "1.8.3"
import django

if django.VERSION < (3, 2):
    default_app_config = "rest_framework_tracking.apps.RestFrameworkTrackingConfig"
