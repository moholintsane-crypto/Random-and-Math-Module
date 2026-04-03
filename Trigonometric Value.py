import math

# Get user input for or define your angle in degrees 
angle_degrees = float(input("Enter the angle in degrees: "))

# Convert degrees to radians (Python's trig functions use radians)
angle_radians = math.radians(angle_degrees)

# Calculate values
sine_val = math.sin(angle_radians)
cosine_val = math.cos(angle_radians)
tangent_val = math.tan(angle_radians)

# Display results
print(f"Angle: {angle_degrees}° ({angle_radians})")
print(f"Sine of {angle_degrees}° is: {sine_val}")
print(f"Cosine of {angle_degrees}° is: {cosine_val}")
print(f"Tangent of {angle_degrees}° is: {tangent_val}")