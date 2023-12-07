DIGIT_NAMES = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def is_char_digit(char):
    ascii_code = ord(char)
    return ascii_code >= 48 and ascii_code < 58

def get_first_digit(line):
    for char in line:
        if is_char_digit(char):
            return char
    
    raise ValueError('No digit in line')

def get_first_digit_including_name(line):
    try:
        digit = get_first_digit(line)
        position = line.find(digit)
    except ValueError:
        position = len(line)
    
    for digit_name in DIGIT_NAMES:
        new_position = line.find(digit_name)

        if new_position == -1:
            continue
        elif new_position < position:
            position = new_position
            digit = DIGIT_NAMES[digit_name]
    
    return digit

def get_last_digit_including_name(line):
    try:
        digit = get_last_digit(line)
        position = line.rfind(digit)
    except ValueError:
        position = -1
    
    for digit_name in DIGIT_NAMES:
        new_position = line.rfind(digit_name)

        if new_position > position:
            position = new_position
            digit = DIGIT_NAMES[digit_name]
    
    return digit

def get_last_digit(line):
    reversed_line = "".join(reversed(line))
    last_digit = get_first_digit(reversed_line)

    return last_digit

def get_lines_from_filename(filename):
    with open(filename) as f:
        lines = f.readlines()

    return lines

def sum_first_last_digits(lines):
    total_sum = 0

    for line in lines:
        first_digit = get_first_digit(line)
        last_digit = get_last_digit(line)
        two_digit_number = first_digit + last_digit
        total_sum += int(two_digit_number)
    
    return total_sum

def sum_first_last_digits_including_names(lines):
    total_sum = 0

    for line in lines:
        first_digit = get_first_digit_including_name(line)
        last_digit = get_last_digit_including_name(line)
        two_digit_number = first_digit + last_digit
        total_sum += int(two_digit_number)
    
    return total_sum
        
def solve_part_one():
    input_filename = "Input.txt"
    input_lines = get_lines_from_filename(input_filename)
    total_sum = sum_first_last_digits(input_lines)

    print("Part One:", total_sum)

def solve_part_two():
    input_filename = "Input.txt"
    input_lines = get_lines_from_filename(input_filename)
    total_sum = sum_first_last_digits_including_names(input_lines)

    print("Part Two:", total_sum)

solve_part_one()
solve_part_two()