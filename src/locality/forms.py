from django.core.validators import EMPTY_VALUES
from django.db.models import Q
from django.forms import fields, ValidationError
from django.utils.translation import ugettext_lazy as _

from locality.models import Country


class CountrySelectField(fields.Field):
    """
    A form field that validates its input to iso2 or iso3 abbreviations
    or the name of countries in the database.
    """
    default_error_messages = {
        'invalid': _("Select a Country."),
    }

    def clean(self, value):
        super(CountrySelectField, self).clean(value)

        if value in EMPTY_VALUES:
            return u''

        country = Country.objects.filter(
            Q(name__iexact=value) | Q(iso2__iexact=value) | Q(
                iso3__iexact=value))

        if not country.exists():
            raise ValidationError(self.default_error_messages['invalid'])

        return country[0]


class CountrySelectWidget(fields.Select):
    """
    A select widget that uses all countries in alphabetical order as its choices.
    """

    def __init__(self, attrs=None):
        choices = []
        for country in Country.objects.all().order_by('name'):
            choices.append((country.iso2, country.name,))
        super(CountrySelectWidget, self).__init__(attrs, choices=choices)
