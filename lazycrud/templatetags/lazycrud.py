# coding=utf-8
from __future__ import unicode_literals

import logging

from django.utils.translation import gettext_lazy as _
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.template.defaultfilters import linebreaksbr

from ..utils import fieldlabel as ufieldlabel, fieldvalue as ufieldvalue

logger = logging.getLogger(__name__)

register = template.Library()

@register.filter
def formfieldlabel(form, key):
    return form.fields[key].label

@register.filter
def fieldlabel(obj, key):
    return ufieldlabel(obj, key)

@register.filter
def fieldvalue(obj, key):
    return ufieldvalue(obj, key)

def _get_label_value(obj, key, autoescape):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    label = esc(fieldlabel(obj, key))
    value = fieldvalue(obj, key)
    if hasattr(value, 'get_absolute_url') and not hasattr(value, 'lazycrud_nofollow'):
        value = '<a href="{}">{}</a>'.format(value.get_absolute_url(), esc(value))
    else:
        value = linebreaksbr(esc(value))
    return label, value

@register.filter(needs_autoescape=True)
def dl_item(obj, key, autoescape=None):
    try:
        label, value = _get_label_value(obj, key, autoescape)
        result = '<dt class="col-sm-4">{}</dt><dd class="col-sm-8">{}</dd>'.format(label, value)
    except:
        logger.exception(_('Error rendering the field %s') % key)
        result = '<dt></dt><dd></dd>'
    return mark_safe(result)

@register.filter(needs_autoescape=True)
def list_item(obj, key, autoescape=None):
    label, value = _get_label_value(obj, key, autoescape)
    result = u'<li><strong>{}:</strong> {}</li>'.format(label, value)
    return mark_safe(result)

@register.filter(needs_autoescape=True)
def tr_item(obj, key, autoescape=None):
    label, value = _get_label_value(obj, key, autoescape)
    result = u'<tr><td class="lazycrud-label">{}</td><td class="lazycrud-value">{}</td></tr>'.format(label, value)
    return mark_safe(result)


@register.simple_tag(takes_context=True)
def sort_url(context, field_name):
    """Build a sort URL toggling asc/desc for the given field, resetting pagination."""
    request = context['request']
    params = request.GET.copy()
    current = params.get('o', '')
    params['o'] = f'-{field_name}' if current == field_name else field_name
    params.pop('page', None)
    return f'?{params.urlencode()}'


@register.simple_tag(takes_context=True)
def query_string(context, **kwargs):
    """Return current query string with the given params overridden."""
    request = context['request']
    params = request.GET.copy()
    for key, value in kwargs.items():
        if value is None:
            params.pop(key, None)
        else:
            params[key] = value
    return f'?{params.urlencode()}'
