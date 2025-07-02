import random

def wybierz_liczbe():
    player_choice = input("Podaj liczbe: ")
    computer_choice = random.randint(1, 100)
    wybory = {"gracz" : player_choice, "komputer" : computer_choice }
    return(wybory)

def sprawdz_wybor(gracz, komputer):
    if gracz == komputer:
        return("Zgadłeś")
    elif gracz > komputer:
        return("Twoja liczba jest większa niż komputera")
    else:
        return("Twoja liczba jest mniejsza niż komputera")

