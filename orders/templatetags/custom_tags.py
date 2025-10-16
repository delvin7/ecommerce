from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply two numbers"""
    return value * arg

@register.filter
def sum_cart(items):
    """Sum total price for cart"""
    total = 0
    for item in items:
        total += item.product.price * item.quantity
    return total
