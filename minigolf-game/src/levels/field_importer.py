from levels.field_two import get_field as field2
from levels.field_three import get_field as field3

fields = {2: field2(), 3: field3()}


def get_field(field_number):
    return fields[field_number]


def get_keys():
    return list(fields.keys())
