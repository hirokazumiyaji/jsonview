from django.views.generic.base import ContextMixin, View
from django.http import HttpResponse
from django.utils import simplejson


class JsonResponseMixin(object):
    response_class = HttpResponse
    content_type = 'application/json'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        return HttpResponse(
            content=simplejson.dumps(context),
            **response_kwargs
        )


class JsonView(JsonResponseMixin, ContextMixin, View):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
