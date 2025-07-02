liczba = input("Podaj liczbę: " )
number = int(liczba)
print(f"Podana liczba to {number}")
if number > 0:
    print("Liczba jest większa niż zero")
elif number < 0:
    print("Liczba jest mniejsza niż zero")
else:
    print("Ta liczba to 0")


def sprawdzenie(number):
    if number % 2 == 0:
        print(f"Liczba {number} jest parzysta")
    else:
        print(f"Liczba {number} jest nieparzysta")
parzystosc = sprawdzenie(number)