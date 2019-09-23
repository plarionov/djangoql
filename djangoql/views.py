import json

from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from djangoql.schema import NonRecursiveDjangoQLSchema


@login_required
def get_model_schema(request, model_path):
    """
    Returns json with model schema by given path
    """
    model_cls = apps.get_model(model_path)
    return HttpResponse(
        content=json.dumps(
            NonRecursiveDjangoQLSchema(model_cls).as_dict(),
            indent=2
        ),
        content_type='application/json; charset=utf-8',
    )
