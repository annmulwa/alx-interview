#!/usr/bin/python3

import sys


def print_message(dict_sc, total_file_size):
    """
    Prints the total file size and the count of each status code.

    Args:
        dict_sc (dict): Dictionary of status codes and their counts.
        total_file_size (int): Total size of the files.

    Returns:
        None
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Split the line into parts
        parsed_line = parsed_line[::-1]  # Reverse the parts

        if len(parsed_line) > 2:
            counter += 1

            # Extract file size and status code
            total_file_size += int(parsed_line[0])
            code = parsed_line[1]

            # Update the status code count if the code is known
            if code in dict_sc:
                dict_sc[code] += 1

            # Print the stats after every 10 lines
            if counter == 10:
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    # Print the final stats
    print_message(dict_sc, total_file_size)
