from os import system
import time, random

start_message = """

    Wybierz jedną z opcji

    1 - kamień
    2 - nożyce
    3 - papier
    ...
    0 - zakończ grę :
    
    """
valid_answers = ['0', '1', '2', '3']
while (True):
    
    system('clear')  
    
    user_choice = input(start_message)
    if user_choice in valid_answers:
        user_choice = int(user_choice)
        if user_choice == 0:
            print("Dziękujemy za grę")
            time.sleep(2)
            break
        else:
            computer_pick = random.randint(1, 3)
            print(f'Komputer losuje: {computer_pick}')
            if (computer_pick == 1 and user_choice == 2) or (computer_pick == 2 and user_choice == 3) \
                    or (computer_pick == 3 and user_choice == 1):
                print("Przegrałeś")
            elif (computer_pick == 1 and user_choice == 3) or (computer_pick == 2 and user_choice == 1) \
                    or (computer_pick == 3 and user_choice == 2):
                print("Wygrałeś")
            elif computer_pick == user_choice:
                print("Remis")
            time.sleep(2)
    else:
        print("Podałeś niepoprawną opcję")
        time.sleep(2)
