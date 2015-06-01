import locale
from django.template import Library

register = Library()
def numberformat(value):
    if not value:
        return "0";

    return locale.format("%.2f", value)

register.filter('numberformat', numberformat)
