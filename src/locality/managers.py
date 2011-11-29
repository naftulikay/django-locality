from django.db import models

class TerritoryManager(models.Manager):
	
	def by_country_iso2(self, iso2 = None):
		return self.all() if iso2 == None else self.filter(country__iso2__iexact = iso2).order_by('abbr')

	def by_country_iso3(self, iso3 = None):
		return self.all() if iso3 == None else self.filter(country__iso3__iexact = iso3).order_by('abbr')

	def by_country_id(self, country_id = None):
		return self.all() if country_id == None else self.filter(country__id = country_id).order_by('abbr')
