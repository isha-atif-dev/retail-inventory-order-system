# utils.py
# This file contains helper functions for file operations.
# It is reused by inventory.py and orders.py.


def read_file(file_path):
    """
    Reads all lines from a file and returns them as a list.
    Each line is returned as a string.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
        return lines


def write_file(file_path, lines):
    """
    Overwrites a file with the given list of lines.
    Each item in 'lines' must be a string.
    """
    with open(file_path, "w") as file:
        file.writelines(lines)
