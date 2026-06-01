from typing import List

def read_integers() -> List[int]:
    number_string = input()
    number_string = [int(x) for x in number_string.split(",")]
    return number_string

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())