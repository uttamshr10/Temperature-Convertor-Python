print("Welcome to the Temperature Conversion App.")

fahrenheit = float(input("\nWhat is the given temperature in Fahrenheit: "))

# Conversion
celsius = (fahrenheit-32)*(5/9)
kelvin = celsius + 273.15

# Round temperatures
fa = round(fahrenheit, 4)
cel = round(celsius, 4)
kel = round(kelvin, 4)

print("\nFahrenheit:\t" + str(fa))
print("Celsius:\t" + str(cel))
print("Kelvin:\t\t" + str(kel))
