weight= float(input("Enter your weight:"))
unit= input("kilograms or pounds? K or L:")

if  unit.upper() == "K":
    weight= weight * 2.205
    print (f"Your weight is {round(weight,1)}Lbs")
elif unit.upper()== "L":
    weight= weight / 2.205
    print (f"Your weight is {round(weight,1)}Kgs")
else:
    print(f"Values are INVALID")

