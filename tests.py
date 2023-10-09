import conversions

def test_convertCelsiusToKelvin():
    test_cases = [(0, 273.15), (-273.15, 0), (100, 373.15), (-100, 173.15), (37, 310.15)]
    for c, k in test_cases:
        result = conversions.convertCelsiusToKelvin(c)
        print(f"{c}C is converted to {result}K")
        assert result == k, f"Failed for {c}C to {k}K. Got {result}K instead."


def test_convertCelsiusToFahrenheit():
    test_cases = [(0, 32), (100, 212), (-100, -148), (37, 98.6), (-40, -40)]
    for c, f in test_cases:
        assert conversions.convertCelsiusToFahrenheit(c) == f, f"Failed for {c}C to {f}F"

test_convertCelsiusToKelvin()
test_convertCelsiusToFahrenheit()

import conversions_refactored

def test_convert():
    # Temperature conversions
    assert conversions_refactored.convert('celsius', 'fahrenheit', 0) == 32
    assert conversions_refactored.convert('celsius', 'kelvin', 0) == 273.15
    # ... Add more temperature tests
    
    # Distance conversions
    assert conversions_refactored.convert('mile', 'yard', 1) == 1760
    assert conversions_refactored.convert('mile', 'meter', 1) == 1609.34
    # ... Add more distance tests
    
    # Same unit conversion
    assert conversions_refactored.convert('mile', 'mile', 1) == 1
    
    # Incompatible unit conversion
    try:
        conversions_refactored.convert('mile', 'celsius', 1)
    except conversions_refactored.ConversionNotPossible as e:
        assert str(e) == "Conversion from mile to celsius is not possible"

test_convert()
