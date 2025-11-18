from django import template

register = template.Library()

@register.filter
def index(lst, i):
    """Returns the item at index i from list lst"""
    try:
        return lst[int(i)]
    except (IndexError, ValueError, TypeError):
        return ''

@register.filter
def scientific(value, decimals=2):
    """Formatea un número en notación científica"""
    try:
        if isinstance(value, (int, float)):
            return f"{value:.{decimals}e}"
        return str(value)
    except (ValueError, TypeError):
        return str(value)