from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('locality.views',
	# generate initial data from localflavors for territories
	url(r'^gen/territories/?$', 'generate_territories'),
	# get json of territories either globally or by country
	url(r'^json/territories(?:/(?P<iso2>[A-Z]{2})/?)?$', 'territories_by_country_iso2'),
	url(r'^json/territories(?:/(?P<iso3>[A-Z]{3})/?)?$', 'territories_by_country_iso3'),
	url(r'^json/territories(?:/(?P<country_id>\d+)/?)?$', 'territories_by_country_id'),
	# get xml of territories either globally or by country
	url(r'^xml/territories(?:/(?P<iso2>[A-Z]{2})/?)?$', 'territories_by_country_iso2', { 'to': 'xml', 'mimetype': 'text/xml' }),
	url(r'^xml/territories(?:/(?P<iso3>[A-Z]{3})/?)?$', 'territories_by_country_iso3', { 'to': 'xml', 'mimetype': 'text/xml' }),
	url(r'^xml/territories(?:/(?P<country_id>\d+)/?)?$', 'territories_by_country_id', { 'to': 'xml', 'mimetype': 'text/xml' }),
    url(r'^admin/', include(admin.site.urls)),
)
