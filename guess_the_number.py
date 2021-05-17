from random import randint


def get_number():
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number")
    return result


def guess_the_number():
    secret_number = randint(1, 100)
    given_number = get_number()

    while given_number != secret_number:
        if given_number < secret_number:
            print("To small!")
        else:
            print("To big!")
        given_number = get_number()
    print("You Win!")


if __name__ == '__main__':
    guess_the_number()