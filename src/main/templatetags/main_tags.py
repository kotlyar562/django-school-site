from django import template

register = template.Library()


@register.inclusion_tag('main/_paginations.html', takes_context=True)
def paginations(context,objects):
    request = context['request']
    gets = request.get_full_path().split('?')
    if len(gets)>1:
        gets = gets[-1]
        gets = '?' + gets
    else:
        gets = ''
    if gets:
        if 'page' in gets:
            gets = gets.replace(gets.split('&')[-1], '')
            if not gets:
                gets += '?'
        else:
            if not gets[-1] == '&':
                gets += '&'
    else:
        gets = '?'
    return {'objects': objects, 'request': context['request'], 'gets': gets}


@register.filter
def get_pk(value):
    return value.pk
