
from django import template
import random

register = template.Library()

@register.simple_tag
def food():
	return "Hello"











