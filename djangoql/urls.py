from django.conf.urls import url

from djangoql.views import get_model_schema

urlpatterns = [
    url(r'^model_schema/(?P<model_path>[\w\.]+)$', get_model_schema, name='get_model_schema'),
]
