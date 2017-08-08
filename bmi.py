# This is a short python program to calculate the bmi of a person
# Home-work of dgplug
""""Update required:-----
    1. This is for adults male, make for adults female and children even
    2. Add. a BMI chart
    3. Make a GUI version of it
"""

print ("Ok")


def check(bmi):
    if bmi < 16:
        print("Severe thinness")
    elif bmi >= 16 and bmi < 17:
        print("Moderate thinness")
    elif bmi >= 17 and bmi < 18.5:
        print("Mild thinness")
    elif bmi >= 18.5 and bmi < 25:
        print("Normal")
    elif bmi >= 25 and bmi < 30:
        print("Overweight")
    elif bmi >= 30 and bmi < 35:
        print("Obese Class-1")
    elif bmi >= 35 and bmi < 40:
        print("Obese Class-2")
    elif bmi >= 40:
        print("Obese Class-3")

# print ("we want to calculate your BMI Press 1. to continue")
ch = int(input("We want to calculate your BMI\nPress 1 to continue\n"))

if ch == 1:
    print("Pressed 1")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in metres: "))
    bmi = weight/(height*height)
    ch2 = int(input("\nTo check your Category\nPress 1\n"))
    if ch2 == 1:
        print("BMI: ",bmi)
        check(bmi)
