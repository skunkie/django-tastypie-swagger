from tastypie_swagger.views import Swagger2View, SwaggerSpecs2View
try:
    from django.urls import  include, path
except ImportError:
    try:
        from django.conf.urls import patterns, include, url
    except ImportError:
        from django.conf.urls.defaults import patterns, include, url


app_name = 'tastypie_swagger'

urlpatterns = [
    path('', Swagger2View.as_view(), name='index'),
    path('specs/swagger.json', SwaggerSpecs2View.as_view(), name='specs'),
]
