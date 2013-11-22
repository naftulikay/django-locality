from re import match

from django.db import models
from django.db.models import Q
from django.http import Http404


class CountryManager(models.Manager):
    def find(self, identifier):
        if type(identifier) is int or match(r'^\d+', identifier):
            return self.get(pk=identifier)
        else:
            return self.get(
                Q(iso2__iexact=identifier) |
                Q(iso3__iexact=identifier) |
                Q(name__iexact=identifier)
            )

    def find_or_404(self, identifier):
        try:
            return self.find(identifier)
        except:
            raise Http404


class TerritoryManager(models.Manager):
    def by_country(self, country=None):
        if type(country) is int or match(r'^\d+$', country):
            return self.filter(country__id=country)

        return self.all() if country == None else self.filter(
            Q(country__iso2__iexact=country) |
            Q(country__iso3__iexact=country) |
            Q(country__name__iexact=country)
        )

    def by_country_iso2(self, iso2=None):
        return self.all() if iso2 == None else self.filter(
            country__iso2__iexact=iso2).order_by('abbr')

    def by_country_iso3(self, iso3=None):
        return self.all() if iso3 == None else self.filter(
            country__iso3__iexact=iso3).order_by('abbr')

    def by_country_id(self, country_id=None):
        return self.all() if country_id == None else self.filter(
            country__id=country_id).order_by('abbr')
