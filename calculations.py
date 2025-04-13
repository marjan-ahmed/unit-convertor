def length_calc(from_unit: str, resultant_unit: str, value: int):
    if from_unit == 'km' and resultant_unit == 'm':
        return value * 1000
    elif from_unit == 'km' and resultant_unit == 'cm':
        return value * 100000
    elif from_unit == 'km' and resultant_unit == 'mm':   
        return value * 1000000
    elif from_unit == 'm' and resultant_unit == 'km':
        return value / 1000
    elif from_unit == 'm' and resultant_unit == 'cm':
        return value * 100
    elif from_unit == 'm' and resultant_unit == 'mm':
        return value * 1000
    elif from_unit == 'cm' and resultant_unit == 'km':
        return value / 100000
    elif from_unit == 'cm' and resultant_unit == 'm':
        return value / 100
    elif from_unit == 'cm' and resultant_unit == 'mm':
        return value * 10
    elif from_unit == 'mm' and resultant_unit == 'km':
        return value / 1000000
    elif from_unit == 'mm' and resultant_unit == 'm':
        return value / 1000
    elif from_unit == 'mm' and resultant_unit == 'cm':
        return value / 10
    else:
        return value
    
def mass_calc(from_unit: str, resultant_unit: str, value: int):
    if from_unit == 'kg' and resultant_unit == 'g':
        return value * 1000
    elif from_unit == 'kg' and resultant_unit == 'mg':
        return value * 1000000
    elif from_unit == 'g' and resultant_unit == 'kg':
        return value / 1000
    elif from_unit == 'g' and resultant_unit == 'mg':
        return value * 1000
    elif from_unit == 'mg' and resultant_unit == 'kg':
        return value / 1000000
    elif from_unit == 'mg' and resultant_unit == 'g':
        return value / 1000
    else:
        return value

def time_calc(from_unit: str, resultant_unit: str, value: int):
    if from_unit == 's' and resultant_unit == 'm':
        return value / 60
    elif from_unit == 's' and resultant_unit == 'h':
        return value / 3600
    elif from_unit == 'm' and resultant_unit == 's':
        return value * 60
    elif from_unit == 'm' and resultant_unit == 'h':
        return value / 60
    elif from_unit == 'h' and resultant_unit == 's':
        return value * 3600
    elif from_unit == 'h' and resultant_unit == 'm':
        return value * 60
    else:
        return value
    
def temp_calc(from_unit: str, resultant_unit: str, value: int):
    if from_unit == 'C' and resultant_unit == 'F':
        return (value * 9/5) + 32
    elif from_unit == 'C' and resultant_unit == 'K':
        return value + 273.15
    elif from_unit == 'F' and resultant_unit == 'C':
        return (value - 32) * 5/9
    elif from_unit == 'F' and resultant_unit == 'K':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K' and resultant_unit == 'C':
        return value - 273.15
    elif from_unit == 'K' and resultant_unit == 'F':
        return (value - 273.15) * 9/5 + 32
    else:
        return value