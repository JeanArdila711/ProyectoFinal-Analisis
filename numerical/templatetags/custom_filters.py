from django import template

register = template.Library()

@register.filter
def index(lst, i):
    """Returns the item at index i from list lst"""
    try:
        return lst[int(i)]
    except (IndexError, ValueError, TypeError):
        return ''
