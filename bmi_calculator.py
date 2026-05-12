# BMI calculator
# BMI = weight (kg) / height (m)^2
name = input("Enter your name: ")
while True:
    try:
        height = float(input("Enter your height in meters: "))
        if height <= 0:
            print("  ⚠  Please enter a positive number for height (greater than 0).")
            continue
        if height > 9:
            print("  ⚠  Please enter a realistic height in meters (e.g. 1.75).")
            continue
        break
    except ValueError:
        print("  ⚠  Invalid input. Please enter a numeric value for height (e.g. 1.75).")
while True:
    try:
        weight = float(input("Enter your weight in kilograms: "))
        if weight <= 0:
            print("  ⚠  Please enter a positive number for weight (greater than 0).")
            continue
        break
    except ValueError:
        print("  ⚠  Invalid input. Please enter a numeric value for weight (e.g. 70).")
bmi = round(weight / (height ** 2), 2)
print(f"Your BMI is: {bmi}")
underweight = bmi < 18.5
normalweight = 18.5 <= bmi < 25
overweight = 25 <= bmi < 30
if underweight:
    category = "Underweight"
elif normalweight:
    category = "Normal weight"
elif overweight:
    category = "Overweight"
else:
    category = "Obese"
print(f"\nName: {name} \nBMI: {bmi} \nCategory: {category}")