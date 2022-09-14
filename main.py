from copy import deepcopy
from pathlib import Path

def is_correct_position(current_waffle, end_waffle, position):
    """
    Check if a position contains the correct letter

    :param current_waffle: The waffle to check
    :param end_waffle: The correct waffle
    :param position: The position (x, y) to check
    :return: a boolean that tells if position contains the correct letter
    """

    return current_waffle[position[0]][position[1]] == end_waffle[position[0]][position[1]]

def swap(current_waffle, end_waffle, a, b):
    """
    Swap letter in position [a_x, a_y] with letter in position [b_x, b_y]

    :param current_waffle: The current waffle
    :param end_waffle: The correct waffle
    :param a: the position to swap
    :param b: the position to be swapped
    :return: the modified waffle, and a boolean that tells if a swap has happened
    """

    if is_correct_position(start_waffle, end_waffle, a) or is_correct_position(start_waffle, end_waffle, b):
        # a or b are already correct, return original waffle
        return current_waffle, False

    if current_waffle[a[0]][a[1]] == '_' or current_waffle[b[0]][b[1]] == '_':
        # swapping with space is not a legal move, return original waffle
        return current_waffle, False

    swapped_waffle = deepcopy(current_waffle)
    swapped_waffle[a[0]][a[1]] = current_waffle[b[0]][b[1]]
    swapped_waffle[b[0]][b[1]] = current_waffle[a[0]][a[1]]

    return swapped_waffle, True

def count_correct_letters(current_waffle, end_waffle):
    """
    Count how many correct letters are in the current waffle.

    :param current_waffle: The current waffle
    :param end_waffle: The correct waffle
    :return: Number of correct letters
    """
    total = 0
    for a_x in range(0, 5):
        for a_y in range(0, 5):
            if current_waffle[a_x][a_y] == end_waffle[a_x][a_y]:
                total += 1
    return total

def generate_permutation(start_waffle, end_waffle):
    """
    Find the best (highest number of correct letters) permutation of the current waffle.

    :param current_waffle: The current waffle
    :param end_waffle: The correct waffle
    :return: The best waffle found with a single swap
    """
    best_waffle = deepcopy(start_waffle)
    current_best = count_correct_letters(start_waffle, end_waffle)
    for a_x in range(0, 5):
        for a_y in range(0, 5):
            if start_waffle[a_x][a_y] != end_waffle[a_x][a_y]:
                for b_x in range(0, 5):
                    for b_y in range(0, 5):
                        if (a_x, a_y) != (b_x, b_y) and start_waffle[b_x][b_y] != end_waffle[b_x][b_y]:
                            new_waffle, swapped = swap(start_waffle, end_waffle, (a_x, a_y), (b_x, b_y))
                            if swapped:
                                new_total = count_correct_letters(new_waffle, end_waffle)
                                if new_total > current_best:
                                    current_best = new_total
                                    best_waffle = deepcopy(new_waffle)
    return best_waffle

def print_waffle(waffle):
    """
    Print a waffle

    :param waffle: The waffle to print
    """
    for row in waffle:
        for element in row:
            print(element, end= ' ')
        print()
    print()

def read_waffle(path):
    """
    Read a waffle from a file

    :param path: The path of the file containing the waffle
    :return: The waffle
    """
    new_waffle = []
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        for l in lines:
            split_line = l.strip().split(' ')
            waffle_row = []
            for elem in split_line:
                waffle_row.append(elem)
            new_waffle.append(waffle_row)
    return new_waffle

waffle_number = input('which waffle do you want to solve? (only numbers) ').zfill(3)
if not waffle_number.isnumeric():
    print('input is not numeric')
    exit(-1)

waffle_path = Path(".", "waffles", waffle_number)
waffle_path_start = Path(waffle_path, "start.txt")
waffle_path_end = Path(waffle_path, "end.txt")

start_waffle = read_waffle(waffle_path_start)
end_waffle = read_waffle(waffle_path_end)

# start_waffle = update_letter_values(start_waffle, end_waffle)

print_waffle(start_waffle)
current_waffle = deepcopy(start_waffle)
i = 0
while (current_waffle != end_waffle and i < 100):
    new_waffle = generate_permutation(current_waffle, end_waffle)
    current_waffle = deepcopy(new_waffle)
    print_waffle(current_waffle)
    input("Press ENTER to continue...")
    i += 1

print('number of steps:', i)