import json

from django import template


register = template.Library()


@register.filter()
def lista_nombre_vacunas(queryset):
    return json.dumps([{
        'id': vacuna.id,
        'nombre': vacuna.nombre,
    } for vacuna in queryset])

