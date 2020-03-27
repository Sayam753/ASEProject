from django import template

register = template.Library()


@register.filter(name='isinstance_tag')
def isinstance_tag(value, data_type):
    if data_type == "list":
        return True if isinstance(value, list) else False
    elif data_type == "dict":
        return True if isinstance(value, dict) else False
    elif data_type == "any":
        if isinstance(value, int) or isinstance(value, float) or isinstance(value, str):
            return True
        return False
