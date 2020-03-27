from django import template

register = template.Library()


@register.filter(name='any_tag')
def any_tag(value, empty):
    return True if any(value.values()) else False
