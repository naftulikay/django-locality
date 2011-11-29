from django.core import serializers
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils.encoding import force_unicode
from django.utils.functional import Promise

from locality.models import Country, Territory

import simplejson as json

def countries(request, to = "json", mimetype = "application/json"):
	return HttpResponse(serializers.serialize(to, Country.objects.all()), mimetype="%s; charset=utf-8" % mimetype)

def territories(request, to = "json", mimetype = "application/json"):
	return HttpResponse(serializers.serialize(to, Territory.objects.all()), mimetype="%s; charset=utf-8" % mimetype)

def territories_by_country_iso2(request, iso2 = None, to = "json", mimetype = "application/json"):
	return HttpResponse(serializers.serialize(to, Territory.objects.by_country_iso2(iso2)), mimetype="%s; charset=utf-8" % mimetype)

def territories_by_country_iso3(request, iso3 = None, to = "json", mimetype = "application/json"):
	return HttpResponse(serializers.serialize(to, Territory.objects.by_country_iso3(iso3)), mimetype="%s; charset=utf-8" % mimetype)

def territories_by_country_id(request, country_id = None, to = "json", mimetype = "application/json"):
	return HttpResponse(serializers.serialize(to, Territory.objects.by_country_id(country_id)), mimetype="%s; charset=utf-8" % mimetype)

def countries(request, to = "json", mimetype = "application/json"):
	return HttpResponse(serializers.serialize(to, Country.objects.all()), mimetype="%s; charset=utf-8" % mimetype)

def country_by_iso2(request, iso2 = None, to = "json", mimetype = "application/json"):
	return HttpResponse(serializers.serialize(to, get_object_or_404(Country, iso2__iexact = iso2)), mimetype="%s; charset=utf-8" % mimetype)

def country_by_iso3(request, iso3 = None, to = "json", mimetype = "application/json"):
	return HttpResponse(serializers.serialize(to, get_object_or_404(Country, iso3__iexact = iso3)), mimetype="%s; charset=utf-8" % mimetype)

def country_by_id(request, country_id = None, to = "json", mimetype = "application/json"):
	return HttpResponse(serializers.serialize(to, get_object_or_404(Country, pk = country_id)), mimetype="%s; charset=utf-8" % mimetype)

def generate_territories(request):
	from django.contrib.localflavor.ar import ar_provinces
	from django.contrib.localflavor.au import au_states
	from django.contrib.localflavor.at import at_states
	from django.contrib.localflavor.be import be_provinces
	from django.contrib.localflavor.br import br_states
	from django.contrib.localflavor.ca import ca_provinces
	from django.contrib.localflavor.de import de_states
	from django.contrib.localflavor.nl import nl_provinces
	from django.contrib.localflavor.in_ import in_states
	from django.contrib.localflavor.it import it_province
	from django.contrib.localflavor.mx import mx_states
	from django.contrib.localflavor.es import es_provinces
	from django.contrib.localflavor.ch import ch_states
	from django.contrib.localflavor.tr import tr_provinces
	from django.contrib.localflavor.us import us_states
	
	counter = SuperCounter(start = 1)
	c = counter

	output = []
	output.extend(create_territories("AR", ar_provinces.PROVINCE_CHOICES, c))
	output.extend(create_territories("AU", au_states.STATE_CHOICES, c))
	output.extend(create_territories("AT", at_states.STATE_CHOICES, c))
	output.extend(create_territories("BE", be_provinces.PROVINCE_CHOICES, c))
	output.extend(create_territories("BR", br_states.STATE_CHOICES, c))
	output.extend(create_territories("CA", ca_provinces.PROVINCE_CHOICES, c))
	output.extend(create_territories("DE", de_states.STATE_CHOICES, c))
	output.extend(create_territories("NL", nl_provinces.PROVINCE_CHOICES, c))
	output.extend(create_territories("IN", in_states.STATE_CHOICES, c))
	output.extend(create_territories("IT", it_province.PROVINCE_CHOICES, c))
	output.extend(create_territories("MX", mx_states.STATE_CHOICES, c))
	output.extend(create_territories("ES", es_provinces.PROVINCE_CHOICES, c))
	output.extend(create_territories("CH", ch_states.STATE_CHOICES, c))
	output.extend(create_territories("TR", tr_provinces.PROVINCE_CHOICES, c))
	output.extend(create_territories("US", us_states.STATE_CHOICES, c))

	return HttpResponse(LazyEncoder(indent="\t").encode(output), mimetype="application/json; charset=utf-8")
	
def create_territories(country_abbr, territories, counter):
	result = []
	country = Country.objects.get(iso2=country_abbr)
	
	for territory in territories:
		result.append({ 
		'model': "locality.territory",
		'pk': counter.get(),
		'fields': {
			'abbr': territory[0], 
			'name': territory[1], 
			'country': country.id 
		}})

		counter.increment()

	return result

class LazyEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Promise):
			return force_unicode(obj)
		return super(LazyEncoder, self).default(obj)

class SuperCounter():
	__current__ = 0

	def __init__(self, start = 0):
		self.__current__ = start

	def get(self):
		return self.__current__

	def increment(self):
		self.__current__ = self.__current__ + 1
		return self.__current__
