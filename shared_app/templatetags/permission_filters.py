from django import template

register = template.Library()


@register.filter(name='has_permission')
def has_permission(user, permission):
    return user.has_perm(permission)


@register.filter
def get_element_at_index(array, parent_index):
    print(array)
    print(parent_index)
    return array[parent_index]



