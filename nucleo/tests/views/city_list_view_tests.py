from nucleo.views import CityListView


def test_city_list_view_context(rf):
    request = rf.get('/cidades/')
    view = CityListView()
    view.setup(request)
    view.object_list = view.get_queryset()  # <-- necessário para ListView

    context = view.get_context_data()
    assert 'cidades' in context
    assert 'algoritmos' in context