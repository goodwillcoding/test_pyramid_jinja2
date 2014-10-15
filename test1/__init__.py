from pyramid.config import Configurator
from test1.models import get_root

def main(global_config, **settings):
    """ This function returns a WSGI application.

    It is usually called by the PasteDeploy framework during
    ``paster serve``.
    """
    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'test1')

    config = Configurator(root_factory=get_root, settings=settings)
    config.add_static_view('static', 'static')
    config.add_route('hello_world', '/')
    config.scan()
    return config.make_wsgi_app()
