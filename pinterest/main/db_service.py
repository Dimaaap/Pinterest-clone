from .filters import EqualFilter


def get_data_from_model(model, field, value):
    eq_filter = EqualFilter()
    result = model.objects.get(**eq_filter(field, value))
    return result



