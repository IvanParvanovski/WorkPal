from django import template

register = template.Library()


@register.filter(name='has_permission')
def has_permission(user, permission):
    permission_codename_lower = permission.lower().replace(" ", "_")
    return user.has_perm(permission_codename_lower)


@register.filter
def get_element_at_index(array, parent_index):
    return array[parent_index]



