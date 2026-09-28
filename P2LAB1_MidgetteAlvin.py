# Alvin Midgette
# September 27, 2026
# P2LAB1
# This program prompts the user for a circle's radius as a float, 
# then calculates and displays its diameter, circumference, and area 
# with specific decimal formatting.

import math

def main():
    # Pseudocode:
    # 1. Prompt user for radius and convert to float
    # 2. Calculate diameter (2 * radius)
    # 3. Calculate circumference (2 * pi * radius)
    # 4. Calculate area (pi * radius squared)
    # 5. Print results with specified decimal formatting (.1f, .2f, .3f)

    # Get the radius from the user as a float
    radius = float(input("Enter the radius of the circle: "))
    
    # Perform calculations
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    
    # Display formatted outputs
    print(f"\nDiameter: {diameter:.1f}")
    print(f"Circumference: {circumference:.2f}")
    print(f"Area: {area:.3f}")

if __name__ == "__main__":
    main()