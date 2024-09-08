height = float(input("Enter your height in centimeters (cms): "))

weight = float(input("Enter your weight in kg: "))

height = height / 100

BMI = weight / (height ** 2)

print("Your Body Mass Index is ", BMI)

if BMI > 0:
    print("You are severley underweight")

elif BMI <= 18:
    print("You are underweight")

elif BMI <= 25:
    print("You are Healthy")

elif BMI <= 30:
    print("You are Overweight")

else:
    print("Please enter correct values")