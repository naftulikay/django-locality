from django.db import models
from django.utils.translation import ugettext_lazy as _

class Country(models.Model):
	iso2 = models.CharField('ISO 3166-1 Alpha 2 Name', max_length=2, unique=True)
	iso3 = models.CharField('ISO 4166-1 Alpha 3 Name', max_length=3, unique=True)
	name = models.CharField('Country Name', max_length=32, unique=True)

	@property
	def abbr(self):
		return self.iso2

	class Meta:
		verbose_name = _('Country')
		verbose_name_plural = _('Countries')
		ordering = ('abbr', 'name',)

	class Admin:
		list_display = ('abbr', 'name',)

class Territory(models.Model):
	abbr = models.CharField('Territory Abbreviation', max_length=2)
	name = models.CharField('Territory Name', max_length=32)
	country = models.ForeignKey('Country', related_name="territories", on_delete=models.CASCADE)

	class Meta:
		verbose_name = _('Territory')
		verbose_name_plural = _('Territories')
		ordering = ('abbr', 'name',)

	class Admin:
		list_display = ('abbr', 'name',)
