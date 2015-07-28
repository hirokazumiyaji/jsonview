from django.views.generic.base import ContextMixin, View
from django.http import HttpResponse

try:
    from django.conf.settings import JSONSerializer as json
except ImportError:
    import json


class JSONResponseMixin(object):
    response_class = HttpResponse
    content_type = 'application/json; charset=UTF-8'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['content_type'] = self.content_type
        return self.response_class(
            content=json.dumps(context, ensure_ascii=False),
            **response_kwargs
        )


class JSONView(JsonResponseMixin, ContextMixin, View):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
