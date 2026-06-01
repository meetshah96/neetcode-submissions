def add_two_numbers() -> int:
    numbers = input()
    number1, number2 = numbers.split(",")
    addition = int(number1) + int(number2)
    return addition


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
