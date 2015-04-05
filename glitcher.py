#!/usr/bin/python

import random
import argparse


def glitch_image(input_file_name, output_file_name=None):
    if output_file_name is None:
        head, tail = input_file_name.split('.')
        output_file_name = '{}-glitched.{}'.format(head, tail)

    # Open the input file in 'read byte' mode
    input_file = open(input_file_name, 'rb')

    # Open the output file in 'write byte' mode
    output_file = open(output_file_name, 'wb')

    # Open and the close the output file
    with output_file as out:
        # Iterate over each line of bytes from the original file
        for line in input_file:
            # Get a random value between 1 and 10000
            rand = random.randint(1, 10000)

            # Check if the random value is 2, 4, 6 or 8
            if rand in (2, 4, 6, 8):
                # Multiply the current line of bytes by the random value
                line *= rand

            # Write the processed line in the output file
            out.write(line)

if __name__ == '__main__':
    # Create the arguments parser instance
    parser = argparse.ArgumentParser(description='Generate a new '
                                                 'glitched image.')

    # Add the input file argument to the arguments parser
    parser.add_argument('input_file_name',
                        help='location of the original file')

    # Add the output file argument to the arguments parser
    parser.add_argument('--output_file_name', default=None,
                        help='location of the target file')

    # Parse the user input arguments
    args = parser.parse_args()

    # Generate the glitched instance based on the arguments
    glitch_image(args.input_file_name, args.output_file_name)
