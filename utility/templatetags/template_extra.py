from django import template
from django.template.defaultfilters import stringfilter,safe
from django.urls import reverse

from django.utils.safestring import mark_safe
import markdown as md

register = template.Library()


@register.filter()
def markdown(value):
    extensions=[
        'markdown.extensions.codehilite',  # Hilight code with specific line 
        'markdown.extensions.fenced_code', # 
        'markdown.extensions.legacy_attrs',
        # Easily put class name inside md 
        'markdown.extensions.nl2br', # Treating new line as line break
        'markdown.extensions.extra',
        # 'abbr'
        ]
    value_ = md.markdown(value,extensions=extensions)
    return mark_safe(value_)

def md_safe(value):
    extensions=[
        'markdown.extensions.codehilite',  # Hilight code with specific line 
        'markdown.extensions.fenced_code', # 
        'markdown.extensions.legacy_attrs',
        # Easily put class name inside md 
        'markdown.extensions.nl2br', # Treating new line as line break
        'markdown.extensions.extra',
        # 'abbr'
        ]
    value_ = md.markdown(value,extensions=extensions)
    return mark_safe(value_)

@register.filter()
def parent_url(request):
    app_name = request.resolver_match.__dict__['app_name']
    url = reverse(app_name+":home")
    return url

@register.filter()
def parent_name(request):
    app_name = request.resolver_match.__dict__['app_name']
    return app_name