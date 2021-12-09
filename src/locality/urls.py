from django.conf.urls import url
from django.contrib import admin
from locality.views import countries, territories, territories_by_country, country, generate_territories

admin.autodiscover()

urlpatterns = [
    # generate initial data from localflavors for territories
    # url(r'^json/generate/territories/?$', generate_territories, name='generate_territories'),

    # get all countries
    url(r'^(?P<to>(?:json|xml|yaml))/countries/(?:all/?)?$', countries, name='countries'),
    # get all territories
    url(r'^(?P<to>(?:json|xml|yaml))/territories/(?:all/?)?$', territories, name='territories'),
    # get territories by country
    url(r'^(?P<to>(?:json|xml|yaml))/territories(?:/(?P<country>(?:\d+|\w{2}|\w{3}))/?)?$',
        territories_by_country, name='territories_by_country'),
    # get country
    url(r'^(?P<to>(?:json|xml|yaml))/country/(?P<country>(?:\d+|\w{2}|\w{3}))/?$',
        country, name='country'),
    #url(r'^admin/', include(admin.site.urls)),
]
