"""This file contains the utility functions"""
from digital_market import env_sets
# ----------------------------------------------------------------------------


def load_from_file(filename: str) -> str | None:
    """This function loads the data from the provided file
    :param filename: the string representing the filename
    :return: the string representing data extracted from the file or None if
    the file is not found
    """
    try:
        with open(filename, encoding='utf-8') as fin:
            result = fin.read()
    except Exception as e:
        print(f"Could not read file, exception: {e}")
        result = None

    return result


def get_description() -> str:
    """This function returns the description for the swagger
    :return: the string representing the description
    """
    description = load_from_file(env_sets.DESCRIPTION_FILE)
    return description or env_sets.DESCRIPTION
