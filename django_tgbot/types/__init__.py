import json


def validate_type_object(obj):
    if obj is None:
        return {}
    if type(obj) == dict:
        return obj

    if type(obj) == str:
        try:
            return json.loads(obj)
        except ValueError:
            return {}

    return {}


def parse_field_configured(obj, config):
    """
    Parses an object to a Telegram Type based on the configuration given
    :param obj: The object to parse
    :param config: The configuration:
        - is array?
        - is array in array?
        - type of the class to be loaded to
    :return: the parsed object
    """
    foreign_type = config if type(config) != dict else config['class']
    if type(config) == dict:

        if 'array' in config and config['array'] is True:
            return [foreign_type(x) for x in obj]

        elif 'array_of_array' in config and config['array_of_array'] is True:
            res = []
            for inner_obj in obj:
                res.append([foreign_type(x) for x in inner_obj])
            return res

    return foreign_type(obj)


class BasicType:
    """
    Types should have an attribute named `fields` with this format in order to be parsed:
    fields = {
        'key': SomeType (Message, str, ...),
        'key': {
            'class': SomeType (Message, str, ...),
            'array': True/False,
            'array_of_array': True/False,
            'validation': True/False
        }
    }
    """
    def __init__(self, obj=None):
        self.obj = validate_type_object(obj)
        self.parse_fields()

    def parse_fields(self):
        if self.obj is None:
            return
        for key in self.fields.keys():
            if key in self.obj:
                try:
                    setattr(
                        self,
                        key,
                        parse_field_configured(self.obj[key], self.fields[key])
                    )
                except ValueError:
                    pass

    def to_dict(self):
        result = {}
        for field in self.fields.keys():
            if not hasattr(self, field):
                continue
            if not hasattr(getattr(self, field), 'to_dict'):
                if type(getattr(self, field)) == list:
                    result[field] = self.make_primitive(getattr(self, field))
                else:
                    result[field] = getattr(self, field)
            else:
                result[field] = getattr(self, field).to_dict()
        return result

    @staticmethod
    def make_primitive(obj):
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()

        if type(obj) == list:
            return [BasicType.make_primitive(x) for x in obj]

        return {}

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def bool_interpreter(x):
        return True if x in [True, 'true', 'True', 1, 'T', 't', '1'] else False

    @classmethod
    def a(child_class, **kwargs):
        if not hasattr(child_class, 'fields'):
            return

        result = child_class()

        for key in child_class.fields.keys():
            if key not in kwargs or kwargs[key] is None:
                continue

            # Validating the argument
            if type(child_class.fields[key]) != dict \
                    or 'validation' not in child_class.fields[key] \
                    or child_class.fields[key]['validation']:

                if type(child_class.fields[key]) == dict:
                    field = child_class.fields[key]
                    if ('array' in field and field['array']) or ('array_of_array' in field and field['array_of_array']):
                        expected_type = list
                    else:
                        expected_type = child_class.fields[key]['class']
                else:
                    expected_type = child_class.fields[key]

                if expected_type == BasicType.bool_interpreter:
                    expected_type = bool

                if type(kwargs[key]) != expected_type:
                    raise ValueError('Type mismatch for argument {}.\nExpected type: {}\nActual type: {}'.format(
                        key, expected_type, type(kwargs[key])
                    ))

            setattr(result, key, kwargs[key])

        return result



