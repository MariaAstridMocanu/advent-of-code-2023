
def get_calibration(text):
    first_digit = "#"
    second_digit = "#"
    for letter in text:
        if first_digit == "#" and second_digit == "#" and str.isdigit(letter):
            first_digit = letter
            second_digit = letter
        if first_digit.isdigit() and letter.isdigit():
            second_digit = letter
    print(first_digit + second_digit)
    return int(first_digit + second_digit)


if __name__ == '__main__':
    with open('calibrations.txt', 'r') as calibrations_file:
        calibrations = []
        for line in calibrations_file:
            calibrations.append(get_calibration(line))
        print("Sum :" + str(sum(calibrations)))