from django.views import generic

from src.apps.refugio.models import Mascota


class VueMinListView(generic.ListView):
    template_name = 'vue/app_min/list.html'
    model = Mascota

