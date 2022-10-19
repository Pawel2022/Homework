
def bmi():
    waga = float(input("waga:"))
    wzrost = float(input("wzrost:"))
    waga/wzrost**2

    if waga/wzrost**2 < 16:
        print("Severe Thinness")
    if waga/wzrost**2 > 16 and waga/wzrost**2 <= 17:
        print("Moderate Thinness")
    if waga/wzrost**2 > 17 and waga/wzrost**2 <= 18.5:
        print("Mild Thinness")
    if waga/wzrost**2 > 18.5 and waga/wzrost**2 <= 25:
        print("Normal")
    if waga/wzrost**2 > 25 and waga/wzrost**2 <= 30:
        print("Overweight")
    if waga/wzrost**2 > 30 and waga/wzrost**2 <= 35:
        print("Obese Class I")
    if waga/wzrost**2 > 35 and waga/wzrost**2 <= 40:
        print("Obese Class II")
    else:
        print("Obese Class III")

bmi()
