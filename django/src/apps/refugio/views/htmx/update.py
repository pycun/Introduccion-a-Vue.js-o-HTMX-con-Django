from django.urls import reverse
from django.views import generic

from src.apps.refugio.forms import MascotaForm
from src.apps.refugio.models import Mascota


class HTMXDetailView(generic.DetailView):
    template_name = 'htmx/update.html'
    model = Mascota


class HTMXUpdateView(generic.UpdateView):
    template_name = 'htmx/_form.html'
    model = Mascota
    form_class = MascotaForm

    def get_success_url(self):
        return reverse('htmx_detail', args=[self.object.id])
