
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file",
                        help="path to pi text file",
                        action="store",
                        required=True)
args = parser.parse_args()


# Open the input file for reading
with open(args.file, 'r') as file:

    # Read the entire contents of the file into a string
    pi_digits = file.read()

# Initialize a dictionary to store the frequency of each digit
digit_frequency = {str(i): 0 for i in range(10)}

# Loop through each digit in the string
for digit in pi_digits:

    # If the digit is a number from 0-9, increment its count in the dictionary
    if digit.isdigit():
        digit_frequency[digit] += 1

# Print the frequency of each digit
for digit, frequency in digit_frequency.items():
    print(f"Digit {digit} occurs {frequency} times.")
