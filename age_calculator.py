name = input("Podaj swoje imię: ")
rok = input("Podaj rok urodzenia: ")
year = int(rok)
if year < 0:
    print("Nie można mieć ujemnej wartości")
else:
    age = 2025 - year
    print(f"Cześć {name}, masz {age} lat")