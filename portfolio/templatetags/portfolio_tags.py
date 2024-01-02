from django import template

register = template.Library()

# This was created for calculating the mod of number
@register.filter
def modulo(num, val):
    return num % val == 0

# This was created for returning the value of list
# This function handled with the (zipped_con_id) ==> it's created with two lists (cat_con, id_con)
# @register.filter
# def value(sequence, position):
#     return sequence[position]