import random
import os


def show_menu():
    os.system("cls")
    print('''
            ¡¡¡ BIENVENID@ A GUESS THE NUMBER !!!
            
            Menu:
            1 - Intenta adivinar el número.
            2 - El ordenador adivina el número
            0 - Salir
            ''')

    option = int(input("Elige una opcion: "))
    os.system("cls")

    if option == 1:
        user_guess_the_number()
    elif option == 2:
        computer_guess_the_number()
    else:
        print("La opción seleccionada no existe. Adiós")


def user_guess_the_number():
    number_to_guess = random.randint(1, 100)
    user_option = int(input(f"Intenta adivinar el número entre 1 y 100: "))

    while user_option != number_to_guess:
        if user_option < number_to_guess:
            user_option = int(input(f"Demasiado bajo! Prueba otra vez: "))
        elif user_option > number_to_guess:
            user_option = int(input(f"Demasiado Alto! Prueba otra vez: "))

    print(f"Lo encontraste, Enhorabuena!! El número era el {number_to_guess}")


def computer_guess_the_number():
    low = 1
    high = 100
    feedback = ''

    input("Piensa un número entre el 1 y el 100. Cuidado! no lo olvides! (Pulsa Intro para empezar)")

    while feedback != 'c':
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low  # could also be high b/c low == high in this else
        feedback = input(f"Es el número {computer_guess} demasiado alto (a), demasiado bajo (b), o (c) si es "
                         f"correcto?:  ").lower()
        if feedback == 'a':
            high = computer_guess - 1
        elif feedback == 'b':
            low = computer_guess + 1

    print(f"YUJUUU! Tú número era el {computer_guess}. Tú ordenador lo ha adivinado!")


show_menu()
