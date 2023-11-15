from django import template
from django.shortcuts import render

register = template.Library()


@register.inclusion_tag("pages/page.html")
def custom_tag(company_name="My Company"):
    return {"company_name": company_name}
