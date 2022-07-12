def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    i=0
    dct={}
    while i<len(cities):
        dct[i]=cities[i]
        i+=1
    return  dct
print(cities_dict(["Bukhara", "Khiva", "Namangan", "Samarkand", "Tashkent"]))