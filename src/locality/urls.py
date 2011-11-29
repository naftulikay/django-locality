from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('locality.views',
	# generate initial data from localflavors for territories
	url(r'^json/generate/territories/?$', 'generate_territories'),
	# get all countries
	url(r'^json/countries/(?:all/?)?$', 'countries'),
	url(r'^xml/countries/(?:all/?)?$', 'countries', { 'to': 'xml', 'mimetype': 'application/xml' }),
	url(r'^yaml/countries/(?:all/?)?$', 'countries', { 'to': 'yaml', 'mimetype': 'application/yaml' }),
	# get all territories
	url(r'^json/territories/(?:all/?)?$', 'territories'),
	# get json of territories either globally or by country
	url(r'^json/territories(?:/(?P<iso2>\w{2})/?)?$', 'territories_by_country_iso2'),
	url(r'^json/territories(?:/(?P<iso3>\w{3})/?)?$', 'territories_by_country_iso3'),
	url(r'^json/territories(?:/(?P<country_id>\d+)/?)?$', 'territories_by_country_id'),
	# get xml of territories either globally or by country
	url(r'^xml/territories(?:/(?P<iso2>\w{2})/?)?$', 'territories_by_country_iso2', { 'to': 'xml', 'mimetype': 'text/xml' }),
	url(r'^xml/territories(?:/(?P<iso3>\w{3})/?)?$', 'territories_by_country_iso3', { 'to': 'xml', 'mimetype': 'text/xml' }),
	url(r'^xml/territories(?:/(?P<country_id>\d+)/?)?$', 'territories_by_country_id', { 'to': 'xml', 'mimetype': 'text/xml' }),
	# get yaml of territories either globally or by country
	url(r'^yaml/territories(?:/(?P<iso2>\w{2})/?)?$', 'territories_by_country_iso2', { 'to': 'yaml', 'mimetype': 'text/yaml' }),
	url(r'^yaml/territories(?:/(?P<iso3>\w{3})/?)?$', 'territories_by_country_iso3', { 'to': 'yaml', 'mimetype': 'text/yaml' }),
	url(r'^yaml/territories(?:/(?P<country_id>\d+)/?)?$', 'territories_by_country_id', { 'to': 'yaml', 'mimetype': 'text/yaml' }),
	# get json of country
	url(r'^json/country/(?P<iso2>\w{2})/?$', 'country_by_iso2'),
	url(r'^json/country/(?P<iso3>\w{3})/?$', 'country_by_iso3'),
	url(r'^json/country/(?P<country_id>\d+)/?$', 'country_by_id'),
   	# get xml of country
 	url(r'^xml/country/(?P<iso2>\w{2})/?$', 'country_by_iso2', { 'to': 'xml', 'mimetype': 'application/xml' }),
	url(r'^xml/country/(?P<iso3>\w{3})/?$', 'country_by_iso3', { 'to': 'xml', 'mimetype': 'application/xml' }),
	url(r'^xml/country/(?P<country_id>\d+)/?$', 'country_by_id', { 'to': 'xml', 'mimetype': 'application/xml' }),
	# get yaml of country
	url(r'^yaml/country/(?P<iso2>\w{2})/?$', 'country_by_iso2', { 'to': 'yaml', 'mimetype': 'application/yaml' }),
	url(r'^yaml/country/(?P<iso3>\w{3})/?$', 'country_by_iso3', { 'to': 'yaml', 'mimetype': 'application/yaml' }),
	url(r'^yaml/country/(?P<country_id>\d+)/?$', 'country_by_id', { 'to': 'yaml', 'mimetype': 'application/yaml' }),
#  	url(r'^admin/', include(admin.site.urls)),
)
