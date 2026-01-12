# Ask the user which unit they want to convert from
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").upper()  # .upper() makes input uppercase (so c or f both work)

# Check if the input unit is valid
if unit not in ("C", "F"):
    print(f"{unit} is invalid. Please enter either C or F.")
else:
    try:
        # Ask for temperature and try to convert it to a number
        temp = float(input("Enter the temperature: "))
    except ValueError:
        # This runs if the user enters something that's not a number (like letters)
        print("Invalid temperature. Please enter a numeric value.")
    else:
        # This block runs only if there was NO error above

        if unit == "C":
            # Check if Celsius value is within valid range
            if temp < -100 or temp > 100:
                print("Please enter a temperature between -100°C and 100°C.")
            else:
                # Convert Celsius to Fahrenheit
                temp = (temp * 9/5) + 32
                print(f"Your temperature is {temp:.2f}°F")

        elif unit == "F":
            # Check if Fahrenheit value is within valid range
            if temp < -148 or temp > 212:
                print("Please enter a temperature between -148°F and 212°F.")
            else:
                # Convert Fahrenheit to Celsius
                temp = (temp - 32) * 5/9
                print(f"Your temperature is {temp:.2f}°C")
