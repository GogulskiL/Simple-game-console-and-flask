from random import randint


def get_number():
    numbers = []
    while len(numbers) != 6:
        try:
            number = int(input("Enter six numbers to draw in range 1-49: "))
            if number in numbers or number < 0 or number > 49:
                print("You have already given such a number or number is out of range")
            else:
                numbers.append(number)
        except ValueError:
            print("It's not a number")
    return numbers


def print_sorted(numbers):
    print(", ".join(str(number) for number in sorted(numbers)))


def draw_numbers():
    result = []
    i = 0
    while i != 6:
        result.append(randint(1, 49))
        i += 1
    return result


def lotto():
    get_numbers = get_number()
    print(f"These are your numbers: ")
    print_sorted(get_numbers)
    draw = draw_numbers()
    print(f"Here are the drawing results: ")
    print_sorted(draw)
    i = 0
    if draw in get_numbers:
        i += 1
    print(f"Number of numbers hit: {i}")
    if i == 3:
        print(f"You hit three!")
    if i == 4:
        print(f"You hit four!")
    if i == 5:
        print(f"You hit five!")
    if i == 6:
        print(f"You hit six!")


if __name__ == '__main__':
    lotto()
