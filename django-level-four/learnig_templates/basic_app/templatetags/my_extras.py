from django import template


register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg, '')

# Utilizando a função sem decorator
# register.filter('cut', cut)