# Length Conversion

def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    # Conversion factors relative to 1 Meter
    units = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }
    
    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported unit provided.")

    # Convert to base unit (meters), then to target unit
    value_in_meters = value * units[from_unit]
    converted_value = value_in_meters / units[to_unit]
    return converted_value

def main():
    print("--- Length Conversion ---")
    
    try:
        val = float(input("Enter length value: "))
        f_unit = input("Enter current unit (mm, cm, m, km, in, ft, yd, mi): ").strip().lower()
        t_unit = input("Enter target unit (mm, cm, m, km, in, ft, yd, mi): ").strip().lower()
        
        result = convert_length(val, f_unit, t_unit)
        print(f"\nResult: {val} {f_unit} = {result:.4f} {t_unit}")
        
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
