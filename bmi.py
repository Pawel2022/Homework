
def bmi():
    waga = float(input("waga:"))
    wzrost = float(input("wzrost:"))
    y =  waga/wzrost**2
    if y < 16:
        print("Severe Thinness")
    if y > 16 and y <= 17:
        print("Moderate Thinness")
    if y > 17 and y <= 18.5:
        print("Mild Thinness")
    if y > 18.5 and y <= 25:
        print("Normal")
    if y > 25 and y <= 30:
        print("Overweight")
    if y > 30 and y <= 35:
        print("Obese Class I")
    if y > 35 and y <= 40:
        print("Obese Class II")
    else:
        print("Obese Class III")

bmi()
