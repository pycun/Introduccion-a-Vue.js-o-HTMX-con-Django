from django.views import generic

from src.apps.refugio.models import Mascota


class HTMXListView(generic.ListView):
    template_name = 'htmx/list.html'
    model = Mascota

