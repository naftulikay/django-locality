from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from locality import managers


class Country(models.Model):
    iso2 = models.CharField('ISO 3166-1 Alpha 2 Name', max_length=2,
                            unique=True)
    iso3 = models.CharField('ISO 3166-1 Alpha 3 Name', max_length=3,
                            unique=True)
    name = models.CharField('Country Name', max_length=128, unique=True)

    objects = managers.CountryManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    @property
    def abbr(self):
        return self.iso2

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ('iso2', 'name',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('iso2', 'iso3', 'name',)


class Territory(models.Model):
    abbr = models.CharField('Territory Abbreviation', max_length=10)
    name = models.CharField('Territory Name', max_length=128)
    country = models.ForeignKey('Country', related_name="territories",
                                on_delete=models.CASCADE)

    objects = managers.TerritoryManager()

    def __str__(self):
        return "%s, %s" % (self.name, self.country.name)

    def __unicode__(self):
        return u"%s, %s" % (self.name, self.country.name)

    class Meta:
        verbose_name = _('Territory')
        verbose_name_plural = _('Territories')
        ordering = ('abbr', 'name',)


class TerritoryAdmin(admin.ModelAdmin):
    list_display = ('abbr', 'country', 'name',)


admin.site.register(Country, CountryAdmin)
admin.site.register(Territory, TerritoryAdmin)
