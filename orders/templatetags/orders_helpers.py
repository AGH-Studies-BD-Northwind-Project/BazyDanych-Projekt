from django import template

register = template.Library()

@register.simple_tag
def multiply2(qty, unitPrice):
    return round(qty * unitPrice, 2)

@register.simple_tag
def multiply3(qty, unitPrice, discount):
    return round(qty * unitPrice * discount, 2)

@register.simple_tag
def substract(minuend, substrahend):
    return minuend - substrahend
