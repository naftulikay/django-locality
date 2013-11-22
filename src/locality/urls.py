from django.conf.urls.defaults import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'locality.views',
    # generate initial data from localflavors for territories
    # url(r'^json/generate/territories/?$', 'generate_territories'),

    # get all countries
    url(r'^(?P<to>(?:json|xml|yaml))/countries/(?:all/?)?$', 'countries'),
    # get all territories
    url(r'^(?P<to>(?:json|xml|yaml))/territories/(?:all/?)?$', 'territories'),
    # get territories by country
    url(r'^(?P<to>(?:json|xml|yaml))/territories(?:/(?P<country>(?:\d+|\w{2}|\w{3}))/?)?$',
        'territories_by_country'),
    # get country
    url(r'^(?P<to>(?:json|xml|yaml))/country/(?P<country>(?:\d+|\w{2}|\w{3}))/?$',
        'country'),
    #url(r'^admin/', include(admin.site.urls)),
)
