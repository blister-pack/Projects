from django import template

register = template.Library()


@register.filter(name="capitalize_words")
def capitalize_word(value):
    return value.title()
