from decimal import Decimal
from fractions import Fraction

import math
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='trim_zeros')
def trim_zeros(value):
    quan = value.quantity

    if value.quantity_type.use_fraction:
        whole = math.floor(quan)
        decimal = quan % 1

        s = str(Decimal(whole))
        s.rstrip('0').rstrip('.') if '.' in s else s

        fraction = Fraction(decimal)

        if fraction.numerator > 0:
            return mark_safe("{0}<sup>{1}</sup>/<sub>{2}</sub>".format(s, fraction.numerator, fraction.denominator))
        else:
            return s
    else:
        s = str(Decimal(quan))
        s.rstrip('0').rstrip('.') if '.' in s else s

        if value.quantity_type.name == "":
            s = "x" + s

        return s
