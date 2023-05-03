"""Commonly used functions

Returns:
    func: funcs
"""
import operator
from phone_iso3166.country import country_prefixes
import flag
import pycountry


def get_countries(placeholder):
    """Create a tuple of country tuples

    Args:
        placeholder (string): the first element in the tuple
        useful when you want a custom option like select country

    Returns:
        tuple: a tuple containing countries and their flags
    """
    countries = []
    countries.append(('', placeholder))
    prefixes = country_prefixes()
    sorted_dict = sorted(prefixes.items(), key=operator.itemgetter(0))
    for item in sorted_dict:
        country = pycountry.countries.get(alpha_2=item[0])
        if country:
            phone_tuple = (
                country.name, f'{flag.flag(item[0])} {country.name}'
            )
            countries.append(phone_tuple)
    return countries
