import json

from django.urls import reverse
from django.views import generic

from src.apps.refugio.forms import MascotaForm
from src.apps.refugio.models import Mascota


class VueMinUpdateView(generic.UpdateView):
    template_name = 'vue/app_min/update.html'
    model = Mascota
    form_class = MascotaForm

    def get_success_url(self):
        return reverse('vue_min_edit', args=[self.object.id])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # NOTE: La variable 'object' que se envia en el context es un Queryset,
        #  Debido a que en los props solo podemos enviar datos serializables,
        #  no podemos enviar en los props de Vue un Queryset.
        #  .
        #  Por lo tanto, le damos un formato json a nuestro Queryset para poder
        #  utilizarlo en los props del componente de vue
        mascota = ctx['object']
        ctx['object_json'] = json.dumps({
            'id': mascota.id,
            'nombre': mascota.nombre,
            'fecha_rescate': mascota.fecha_rescate.strftime("%Y-%m-%d"),
            'edad': mascota.edad,
            'sexo': mascota.sexo,
            'persona': {
                'id': mascota.persona.id,
                'nombre': mascota.persona.nombre,
                'apellidos': mascota.persona.apellidos,
            },
            'vacunas': [{'id': vacuna.id, 'nombre': vacuna.nombre} for vacuna in mascota.vacunas.all()]
        })
        return ctx
