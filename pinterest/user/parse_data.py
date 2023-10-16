import pycountry


def get_list_all_countries():
    countries_list = []
    counter = 1
    for i in pycountry.countries:
        try:
            countries_list.append((i.name, i.name))
            counter += 1
        except AttributeError:
            continue
    return countries_list
