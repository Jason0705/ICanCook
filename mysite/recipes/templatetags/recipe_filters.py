from decimal import Decimal
from fractions import Fraction

import math
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='format_quantity')
def format_quantity(value):
    quan = value.quantity

    if value.quantity_type.use_fraction:
        whole = math.floor(quan)
        decimal = quan % 1

        s = str(Decimal(whole))
        s.rstrip('0').rstrip('.') if '.' in s else s

        fraction = Fraction(decimal)

        output = ""

        if whole > 0:
            output += s

        if fraction.numerator > 0:
            output += ("<sup>{0}</sup>/<sub>{1}</sub>".format(fraction.numerator, fraction.denominator))

        return mark_safe(output)
    else:
        # http://stackoverflow.com/questions/11227620/drop-trailing-zeros-from-decimal
        s = str(Decimal(quan))
        s.rstrip('0').rstrip('.') if '.' in s else s

        if value.quantity_type.name == "":
            s = "x" + s

        return s
