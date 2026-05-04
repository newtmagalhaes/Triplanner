from django.views.generic import ListView
from ..models import City
from ..algoritmos import ALGORITMOS_CHOICES


class CityListView(ListView):
    model = City
    template_name = 'nucleo/city_list.html'
    context_object_name = 'cidades'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['algoritmos'] = ALGORITMOS_CHOICES
        return context