from pyramid.i18n import TranslationStringFactory
from pyramid.view import view_config

_ = TranslationStringFactory('test1')

@view_config(route_name='hello_world', renderer="mytemplate.jinja2")
def my_view(request):
    return {'project':'test1'}
