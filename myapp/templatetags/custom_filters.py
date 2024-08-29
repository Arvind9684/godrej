from django import template

register = template.Library()

@register.filter
def format_views(value):
    try:
        value = int(value)
        if value >= 1000:
            return f'{value/1000:.1f}k'
        return str(value)
    except (ValueError, TypeError):
        return str(value)
