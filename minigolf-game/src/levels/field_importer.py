from levels.field_one import get_field as field1
from levels.field_two import get_field as field2
from levels.field_three import get_field as field3
from levels.field_four import get_field as field4

fields = {1: field1(), 2: field2(), 3: field3(), 4: field4()}


def get_field(field_number):
    return fields[field_number]


def get_keys():
    return list(fields.keys())
