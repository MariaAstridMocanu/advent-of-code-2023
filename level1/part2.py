import re

written = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7",
           "8", "9"]
written_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def get_calibration(text):
    digit_positions = {}
    print(f"[{text.rstrip()}]")
    first_pos = {}
    last_pos = {}

    for written_digit in written:
        if len([m.start() for m in re.finditer(written_digit, text)]) != 0:
            first_pos[written_digit] = (text.find(written_digit))
            last_pos[written_digit] = (text.rfind(written_digit))
            # print(written_digit, f"({text.find(written_digit)}, {text.rfind(written_digit)})")
    print(first_pos)
    print("Selected first: " + min(first_pos, key=first_pos.get))
    print(last_pos)
    print("Selected last: " + max(last_pos, key=first_pos.get))
    print("Result: " + text_to_digit(min(first_pos, key=first_pos.get)) + text_to_digit(max(last_pos, key=first_pos.get)))
    return int(text_to_digit(min(first_pos, key=first_pos.get)) + text_to_digit(max(last_pos, key=last_pos.get)))


def text_to_digit(written_number):
    if not written_number.isdigit():
        return written_digits[written_number]
    else:
        return written_number


if __name__ == '__main__':
    with open('calibrations.txt', 'r') as calibrations_file:
        calibrations = []
        sum = 0
        for line in calibrations_file:
            sum += get_calibration(line)
        print("Sum: " + str(sum))
