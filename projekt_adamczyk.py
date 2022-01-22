import random
import string


def create_list(number_of_items=4, item_lenght=4, item_type='string'):
    """
    Return list with random values.
    Parameters:
    number_of_items: number od items in the created list (default 4)
    item_lenght: lenght of each item in the created list (default 4)
    item_type: type of items, choose 'string' or 'int' type (default 'string')
    Returns:
    list: generated list
    """
    elements = {'string': string.ascii_letters, 'int': range(10)}
    list_of_elements = list()
    get_value_range = elements['int'] if item_type == 'int' else elements['string']
    for _ in range(number_of_items):
        item = ''
        for _ in range(item_lenght):
            item += str(random.choice(get_value_range))
        list_of_elements.append(item)
    return list_of_elements