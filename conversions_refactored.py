class ConversionNotPossible(Exception):
    pass

def convert(from_unit, to_unit, value):
    temp_conversion = {'celsius': {'kelvin': lambda x: x + 273.15, 'fahrenheit': lambda x: x * 9/5 + 32},
                       'fahrenheit': {'celsius': lambda x: (x - 32) * 5/9, 'kelvin': lambda x: (x - 32) * 5/9 + 273.15},
                       'kelvin': {'celsius': lambda x: x - 273.15, 'fahrenheit': lambda x: (x - 273.15) * 9/5 + 32}}
    
    distance_conversion = {'mile': {'yard': lambda x: x * 1760, 'meter': lambda x: x * 1609.34},
                           'yard': {'mile': lambda x: x / 1760, 'meter': lambda x: x * 0.9144},
                           'meter': {'mile': lambda x: x / 1609.34, 'yard': lambda x: x / 0.9144}}
    
    if from_unit in temp_conversion and to_unit in temp_conversion[from_unit]:
        return temp_conversion[from_unit][to_unit](value)
    elif from_unit in distance_conversion and to_unit in distance_conversion[from_unit]:
        return distance_conversion[from_unit][to_unit](value)
    elif from_unit == to_unit:
        return value
    else:
        raise ConversionNotPossible("Conversion from {} to {} is not possible".format(from_unit, to_unit))
