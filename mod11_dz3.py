def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = []
    methods = []
    for attr_name in dir(obj):
        if not attr_name.startswith('__') or not attr_name.endswith('__'):
            attribute = getattr(obj, attr_name)
            if callable(attribute):
                methods.append(attr_name)
            else:
                attributes.append(attr_name)

    module = getattr(obj, "__module__", "__main__")

    return {
        "type": obj_type,
        "attributes": sorted(attributes),
        "methods": sorted(methods),
        "module": module
    }

# Пример работы
number_info = introspection_info(42)
print(number_info)