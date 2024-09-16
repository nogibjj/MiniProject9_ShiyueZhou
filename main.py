"""
Main cli or app entry point
"""

from mylib.calculator import *

def g_describe():
    g = load_dataset()
    return g.describe()

def save_to_md():
    with open("test.md", "a") as file:
        file.write("test")


def main():
    save_to_md()


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
